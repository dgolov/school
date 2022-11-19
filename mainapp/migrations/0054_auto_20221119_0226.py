# Generated by Django 3.2.7 on 2022-11-18 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0053_auto_20221117_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='achievement',
        ),
        migrations.AddField(
            model_name='profile',
            name='achievement',
            field=models.ManyToManyField(blank=True, related_name='achievement', to='mainapp.Achievement', verbose_name='ачивки'),
        ),
    ]