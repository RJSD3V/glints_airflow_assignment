FROM postgres:latest
COPY ./init.sh /docker-entrypoint-initdb.d
COPY ./sql/create_tables.sql /docker-entrypoint-initdb.d