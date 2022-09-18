#!/bin/sh

echo 'Start reloading frontend services'

cd ..

docker stop school_nginx_1
docker rm school_nginx_1
docker rm school_vue_1
docker volume rm school_vue_dist
docker rmi school_vue
docker rmi school_nginx
docker-compose up -d --no-deps --build vue
docker-compose up -d --no-deps --build nginx

echo 'Frontend reloaded successfully'
