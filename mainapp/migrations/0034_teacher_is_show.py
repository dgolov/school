# Generated by Django 3.2.7 on 2022-03-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_remove_profile_is_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='Виден всем'),
        ),
    ]