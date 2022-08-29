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
create table "yeet" ("VendorID" INTEGER, "tpep_pickup_datetime" TEXT, "tpep_dropoff_datetime" TEXT, "passenger_count" INTEGER, "trip_distance"
  REAL, "RatecodeID" INTEGER, "store_and_fwd_flag" TEXT, "PULocationID" INTEGER, "DOLocationID" INTEGER, "payment_type" INTEGER, "fare_amount" REAL, "extra" REAL, "mt
 a_tax" REAL, "tip_amount" REAL, "tolls_amount" REAL, "improvement_surcharge" REAL, "total_amount" REAL, "congestion_surcharge" REAL)