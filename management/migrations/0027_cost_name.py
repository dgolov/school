# Generated by Django 3.2.7 on 2022-01-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0026_auto_20220108_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Наименование затраты'),
        ),
    ]