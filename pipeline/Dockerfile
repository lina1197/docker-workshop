# Use Postgres 18 as base image
FROM postgres:18

# Set environment variables for the database
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=ny_taxi

# Create a directory inside the container for data (matches the volume in your run command)
VOLUME /var/lib/postgresql

# Expose Postgres port
EXPOSE 5432




