

docker run -it --rm \ 
--network=
    taxi_ingest:v001 \ 
        --pg_user=root \
        --pg_pass=root \
        --pg_host=localhost \
        --pg_port=5432 \
        --pg_db=ny_taxi \
        --target_table=yellow_taxi_trips_2021_1 \
        --chunksize=100000

uv run python ingest_data.py \
    --pg_user=root \
    --pg_pass=root \
    --pg_host=localhost \
    --pg_port=5432 \
    --pg_db=ny_taxi \
    --target_table=yellow_taxi_trips_2021_1 \
    --chunksize=100000