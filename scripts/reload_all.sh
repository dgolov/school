#!/bin/sh

echo 'Start reloading all services'

cd ..

docker-compose down
docker rmi school_vue school_web school_daphne
docker volume rm school_vue_dist school_static_volume
docker-compose up --no-deps --build -d
docker-compose exec web python manage.py migrate --noinput

echo 'All services reloaded successfully'