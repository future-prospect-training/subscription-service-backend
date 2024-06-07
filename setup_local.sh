#!/bin/sh
export POSTGRES_USER=bgts
export POSTGRES_PASS=bgts1337
export POSTGRES_DB=default
export POSTGRES_PORT=5432
docker stop $(docker ps -a -q)
docker container prune
docker volume prune
docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_USER=bgts -e POSTGRES_PASSWORD=bgts1337 -e POSTGRES_DB=default postgres:16
docker run -d -p 80:80 --name my-pgadmin -e PGADMIN_DEFAULT_EMAIL=bgts@bgts.com -e PGADMIN_DEFAULT_PASSWORD=bgts1337 dpage/pgadmin4
echo "running"
