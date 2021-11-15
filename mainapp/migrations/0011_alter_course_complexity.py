# Generated by Django 3.2.7 on 2021-11-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_course_color_hex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='complexity',
            field=models.CharField(choices=[('newbie', 'Новичок'), ('user', 'Пользователь'), ('professional', 'Профессионал'), ('cheater', 'Читер')], default='newbie', max_length=50, verbose_name='Сложность'),
        ),
    ]
