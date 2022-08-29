# this script creates a table and loads it in my local postgres container, then select queries it back

import pandas as pd
from sqlalchemy import create_engine

print (pd.__version__)

url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz'

df = pd.read_csv(url, nrows=1000)
print(f'dimensions of: {df.shape[0]} rows and {df.shape[1]} columns')

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

# create engine to local postgres container
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df.to_sql(name='yeet', con=engine, if_exists='append', index=False)

# read data of top 25 most expensive trips
query = """select * from public.yeet order by total_amount desc limit 25;"""

returned_df = pd.read_sql(query, con=engine)

print("hello")
