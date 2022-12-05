# Generated by Django 3.2.7 on 2022-12-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0057_lesson_available_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='available_students',
            field=models.ManyToManyField(blank=True, related_name='available_students', to='mainapp.Student', verbose_name='Обучающиеся кому доступен урок'),
        ),
    ]
