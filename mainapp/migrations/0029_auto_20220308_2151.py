# Generated by Django 3.2.7 on 2022-03-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_alter_course_in_main_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='header',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Заголовок h1'),
        ),
        migrations.AddField(
            model_name='course',
            name='html_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Описание для поисковиков'),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Title'),
        ),
    ]