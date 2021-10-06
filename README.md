# Электронная образовательная среда "Академия будущего"

<img src="https://i.ibb.co/MCvKnJp/image.png" alt="image" border="0" width="200">

###### ООО УК "Академия будущего"

## Используемые технологии:

#### Back-end:
- Python 3.9
- Django 3.2
- Django Rest Framework
- Django Channels
- JWT
- DRF-yasg
- Yookassa API 

#### Front-end:
- JavaScript
- Vue JS

#### Database:
- Postgres

#### Deploy:
- Docker
- Nginx
- Linux

## Запуск dev версии приложения

Для запуска серверной части приложения в корневой директории проекта запустить команду:

`python manage.py runserver`

Для запуска клиенской части:

`cd scool-ui`

`npm run serve`

## Запуск приложения в Docker

Для запуска приложения в Docker в корневой директории проекта выполнить команду:

` docker-compose up --build`

### Остановка Docker

` docker-compose down`

`docker volume rm school_vue_dist`

`docker rmi school_vue school_web school_daphne`