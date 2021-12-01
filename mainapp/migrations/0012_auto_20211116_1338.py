# Generated by Django 3.2.7 on 2021-11-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alter_course_complexity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='course_teachers', to='mainapp.Teacher', verbose_name='Преподаватель курса'),
        ),
    ]