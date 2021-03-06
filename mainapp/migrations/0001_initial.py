# Generated by Django 3.2.7 on 2021-09-28 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainapp.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название Категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': '02. Обучение - Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название курса')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='images/posters', verbose_name='Изображение курса')),
                ('video_presentation', models.SlugField(blank=True, null=True, verbose_name='Ссылка на видеопрезентацию курса')),
                ('is_active', models.BooleanField(default=True, verbose_name='Доступный курс')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': '02. Обучение - Курсы',
            },
        ),
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название диалога')),
                ('is_group', models.BooleanField(default=False, verbose_name='Беседа')),
            ],
            options={
                'verbose_name': 'Диалог',
                'verbose_name_plural': '03. Личные сообщения - Диалоги',
            },
        ),
        migrations.CreateModel(
            name='DialogAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/messages_files', verbose_name='Файл')),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.dialog', verbose_name='Диалог')),
            ],
            options={
                'verbose_name': 'Вложение',
                'verbose_name_plural': '03. Личные сообщения - Вложения в диалогах',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название группы')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': '01. Пользователи - Группы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100, verbose_name='Тема урока')),
                ('video_slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на видеозапись урока')),
                ('lesson_number', models.PositiveIntegerField(default=1, verbose_name='Номер урока в курсе')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание урока')),
                ('materials', models.FileField(blank=True, null=True, upload_to='files/courses/materials', verbose_name='Материалы курса')),
                ('is_active', models.BooleanField(default=True, verbose_name='Доступный урок')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': '02. Обучение - Уроки',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/photos', verbose_name='Изображение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': '04. Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('gender', models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский')], max_length=50, verbose_name='Пол')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('vk_slug', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ссылка на профиль vk.com')),
                ('instagram_slug', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ссылка на профиль instagram')),
                ('date_of_birthday', models.DateField(verbose_name='Дата рождения')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('user_group', models.CharField(choices=[('admin', 'Администратор'), ('manager', 'Менеджер учебного процесса'), ('teacher', 'Преподаватель'), ('student', 'Студент')], default='student', max_length=50, verbose_name='Группа пользователей')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный пользователь')),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='avatar', to='mainapp.photo', verbose_name='Аватарка')),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Пописчики')),
                ('friend_request_in', models.ManyToManyField(blank=True, related_name='in_friends', to=settings.AUTH_USER_MODEL, verbose_name='Входящие заявки в друзья')),
                ('friend_request_out', models.ManyToManyField(blank=True, related_name='out_friends', to=settings.AUTH_USER_MODEL, verbose_name='Исходящие заявки в друзья')),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL, verbose_name='Друзья')),
                ('photos', models.ManyToManyField(blank=True, related_name='photo_list', to='mainapp.Photo', verbose_name='Фотографии')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='EducationalManager',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.profile')),
            ],
            options={
                'verbose_name': 'Менеджер учебного процесса',
                'verbose_name_plural': '01. Пользователи - Менеджеры учебного процесса',
            },
            bases=('mainapp.profile',),
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата и время урока')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Завершен')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.group', verbose_name='Группа')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.lesson', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Рассписание урока',
                'verbose_name_plural': '02. Обучение - Рассписание занятий',
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='for_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='mainapp.Profile', verbose_name='Лайки'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст сообщения')),
                ('date_and_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время сообщения')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('system_message', models.BooleanField(default=False, verbose_name='Системное сообщение')),
                ('attachment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.dialogattachment', verbose_name='Вложение')),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialog', to='mainapp.dialog', verbose_name='Диалог')),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_user', to='mainapp.profile', verbose_name='От кого')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': '03. Личные сообщения - Сообщения',
            },
        ),
        migrations.AddField(
            model_name='dialogattachment',
            name='from_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.profile', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='group_founder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_founder', to='mainapp.profile', verbose_name='Основатель беседы'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dialog_image', to='mainapp.dialogattachment', verbose_name='Изображение диалога'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='last_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_message', to='mainapp.message', verbose_name='Последнее сообщение'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to='mainapp.Profile', verbose_name='Участники диалога'),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/certificates', verbose_name='Изображение')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата вручения')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course', verbose_name='Пройденный курс')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile', verbose_name='Профиль пользователя')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': '02. Обучение - Сертификаты',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.profile')),
                ('education', models.CharField(blank=True, max_length=100, null=True, verbose_name='Образование')),
                ('professional_activity', models.CharField(blank=True, max_length=150, null=True, verbose_name='Профессиональная деятельность')),
                ('courses', models.ManyToManyField(blank=True, related_name='teacher_courses', to='mainapp.Course', verbose_name='Курсы проводимые преподователем')),
                ('group_list', models.ManyToManyField(blank=True, related_name='teacher_groups', to='mainapp.Group', verbose_name='Группы')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': '01. Пользователи - Преподаватели',
            },
            bases=('mainapp.profile',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.profile')),
                ('hobbies', models.TextField(blank=True, null=True, verbose_name='Увлечения')),
                ('dream', models.TextField(blank=True, null=True, verbose_name='Мечта')),
                ('courses', models.ManyToManyField(blank=True, related_name='student_courses', to='mainapp.Course', verbose_name='Доступные курсы')),
                ('group_list', models.ManyToManyField(blank=True, related_name='student_groups', to='mainapp.Group', verbose_name='Группы')),
            ],
            options={
                'verbose_name': 'Обучающийся',
                'verbose_name_plural': '01. Пользователи - Обучающиеся',
            },
            bases=('mainapp.profile',),
        ),
        migrations.AddField(
            model_name='lesson',
            name='is_finished',
            field=models.ManyToManyField(blank=True, related_name='is_finished_lesson', to='mainapp.Student', verbose_name='Обучающиеся завершившие урок'),
        ),
        migrations.AddField(
            model_name='group',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='mainapp.educationalmanager', verbose_name='Менеджер учебного процесса'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='mainapp.teacher', verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_finished',
            field=models.ManyToManyField(blank=True, related_name='is_finished_course', to='mainapp.Student', verbose_name='Обучающиеся завершившие курс'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.teacher', verbose_name='Преподаватель курса'),
        ),
        migrations.CreateModel(
            name='AcademicPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата оценки')),
                ('type_grade', models.CharField(choices=[('homework', 'Домашняя работа'), ('classwork', 'Класная работа'), ('test', 'Контрольная работа'), ('examination', 'Экзамен')], max_length=50, verbose_name='Тип оценки')),
                ('grade', mainapp.models.IntegerRangeField(verbose_name='Оценка')),
                ('late', models.BooleanField(default=False, verbose_name='Опоздание')),
                ('absent', models.BooleanField(default=False, verbose_name='Отсутствие')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.lesson', verbose_name='Урок')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.student', verbose_name='Обучающийся')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Успеваемость',
                'verbose_name_plural': '02. Обучение - Успеваемость',
                'ordering': ['-date'],
            },
        ),
    ]
