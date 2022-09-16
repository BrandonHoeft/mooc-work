# coding: utf-8
import argparse
import os
from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(params):
    """
    ingest CSV data from source and load to target pg database in chunks

    Note: expects command line parameters for DB info [not a good prod practice
    as sensitive plain text CL args get saved to shell history. use configs,
    env vars, password vaults, etc. instead]
    """
    user = params.user  # attribute of args input
    pw = params.pw
    host = params.host
    port = params.port
    database = params.database
    tablename = params.tablename
    url = params.url

    os.system(f"curl {url} -L --output download.csv.gz")  # downloads to working dir
    os.system(f"gzip -d download.csv.gz")  # decompress

    # create engine to local postgres container
    conn_str = f'postgresql://{user}:{pw}@{host}:{port}/{database}'
    engine = create_engine(conn_str)

    # Don't want to try inserting too many rows to db at once, budget with chunks
    df_iter = pd.read_csv(url, iterator=True, chunksize=100000)

    df = next(df_iter)

    # prep column types
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # write a DDL using the column headers/dtypes from first chunk
    df.head(n=0).to_sql(name=tablename, con=engine, if_exists='replace', index=False)

    # write the first data chunk to new table
    df.to_sql(name=tablename, con=engine, if_exists='append', index=False)
    print(f"inserted first chunk of size: {len(df)}")

    while True:

        try:
            t_start = time()  # for performance benchmarking only

            # iterate over next chunk
            df = next(df_iter)

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=tablename, con=engine, if_exists='append', index=False)

            t_end = time()

            print(f"inserted another chunk of size: {len(df)} ... took {round(t_end - t_start)} seconds")

        # once no more next() chunks
        except StopIteration:
            print("Finished ingesting data into the postgres database!")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--pw', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--database', required=True, help='database name for postgres')
    parser.add_argument('--tablename', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)
