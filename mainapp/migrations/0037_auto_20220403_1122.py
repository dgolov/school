# Generated by Django 3.2.7 on 2022-04-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0036_alter_profile_is_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventday',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Ссылка'),
        ),
    ]