# Generated by Django 3.2.7 on 2021-12-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20211204_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='profession',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Профессия'),
        ),
    ]
