# Generated by Django 3.2.7 on 2022-11-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0049_alter_academicperformance_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата завершения занятий'),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала занятий'),
        ),
        migrations.AddField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание группы'),
        ),
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/photos/group', verbose_name='Изображение группы'),
        ),
        migrations.AddField(
            model_name='group',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления'),
        ),
    ]
