# Note: this could be a DOCKERFILE instead of a shell command
# Purpose: build a local dev database on my machine
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_pg_data:/var/lib/postgresql/data:rw \
    -p 5432:5432 \
    postgres:13

# connect to a local pg instance with pgcli
pgcli -h localhost -p 5432 -u root -d <name_of_database>

# example command DDL to throw into pgcli before loading with pandas
CREATE TABLE "yeet" (
  "VendorID" INTEGER,
  "tpep_pickup_datetime" TIMESTAMP,
  "tpep_dropoff_datetime" TIMESTAMP,
  "passenger_count" INTEGER,
  "trip_distance" REAL,
  "RatecodeID" INTEGER,
  "store_and_fwd_flag" TEXT,
  "PULocationID" INTEGER,
  "DOLocationID" INTEGER,
  "payment_type" INTEGER,
  "fare_amount" REAL,
  "extra" REAL,
  "mta_tax" REAL,
  "tip_amount" REAL,
  "tolls_amount" REAL,
  "improvement_surcharge" REAL,
  "total_amount" REAL,
  "congestion_surcharge" REAL
)


# container + docker network + container name (pg-db-container) so pgadmin on
# on same docker host can communicate to my postgres database. video 1.2.3

docker network create pg-network

# $(pwd) should be in ~/PycharmProjects/mooc-work
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/pg_data_ny_taxi:/var/lib/postgresql/data:rw \
    -p 5432:5432 \
    --network=pg-network \
    --name my-postgres \
    postgres:13

# pgadmin4: https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html
docker run -it \
    -e 'PGADMIN_DEFAULT_EMAIL=admin@admin.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=root' \
    -p 8080:80 \
    --network=pg-network \
    --name my-pgadmin \
    dpage/pgadmin4


# running the ingest_data.py pipeline script (targeting a pg container like above)
URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

python -B ingest_data.py /
  --user=root /
  --pw=root /
  --host=localhost /
  --port=5432 /
  --database=ny_taxi /
  --tablename=taxi_yeet_yeet /
  --url=${URL}


