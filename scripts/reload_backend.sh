#!/bin/sh

echo 'Start reloading frontend services'

cd ..

docker stop school_web_1
docker stop school_nginx_1
docker rm school_nginx_1
docker rm school_web_1
docker volume rm school_static_volume
docker rmi school_web
docker rmi school_nginx
docker-compose up -d --no-deps --build web
docker-compose up -d --no-deps --build nginx

echo 'Frontend reloaded successfully'