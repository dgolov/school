# Электронная образовательная среда "Академия будущего"

<img src="https://i.ibb.co/MCvKnJp/image.png" alt="image" border="0" width="200">

###### ООО УК "Академия будущего"

#### Описание

Образовательная платформа с элементами социальной сети. На платформе размещаются обучающие курсы и категории курсов для детей и взрослых. Доступ к курсам предоставляется после онлайн (либо очной) оплаты пользователем. Онлайн оплата осуществляется через систему YOOKASSA (В будущем планируется подключить банк Авангард). Пользователи делятся на несколько категорий с разделенным функционалом: Администратор, менеджер по продажам, менеджер учебного процесса, преподаватель, студент. Проект направлен на улучшение образовательного уровня среди школьников. Основные направления курсов: Программирование, дизайн, шахматы.

#### Социальная сеть

Функционал социальной сети доступен следующей группе пользователей:
- Преподаватели
- Студенты

Общий функционал соц сети предоставляет добавление пользователя в друзья, удаление из друзей, подписка/отписка, фотогалерея с возможностью лайкать фотографии, возможность установить аватарку из галереи, месенджер на веб сокетах, уведомления на веб сокетах, проссмотр учебных групп, электронного дневнка и рассписания. Система поиска по студентам и преподавателям. Настройки профиля. Мини игры. Преподаватели могут вести электронный дневник, ставить оценки, формировать расписание, задавать домашнее задание, формировать описание к уроку, выкладывать ссылку на прямой эфир урока. Студенты могут просматривать рассписание по доступным курсам, успеваемость в элетронном дневнике и домашнее задание, просматривать доступные курсы и материалы к ним. Менеджеры учебного процесса могут формировать группы, рассписание занятий, редактировать курсы и уроки.

#### CRM

На сайте предусмотрена crm система предоставляющая механизм отношения с клиентами и сотрудниками компании. Фронт CRM выполнен на Django Templates. Доступ к разделам системы разделен по следующим группам сотрудников:

- Администраторы (имеют полный доступ)
- Менеджеры по продажам (доступ к разделу продаж)
- Менеджеры учебного процесса (доступ к учебному разделу)
- HR менеджеры (Доступ к кадровому разделу)

## Используемые технологии:

#### Back-end:
- Python 3.9
- Django 3.2
- Django Rest Framework
- Django Channels
- JWT
- DRF-yasg
- Yookassa API 
- Redis

#### Front-end:
- JavaScript
- Vue JS
- Axios
- HTML
- CSS

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

` docker-compose up --build -d`

### Остановка Docker

` docker-compose down`

`docker volume rm school_vue_dist`

`docker rmi school_vue school_web school_daphne`
