#!/bin/sh

echo 'Start reloading nginx service'

cd ..

docker stop school_nginx_1
docker rm school_nginx_1
docker-compose up -d --no-deps --build nginx

echo 'Nginx reloaded successfully'
