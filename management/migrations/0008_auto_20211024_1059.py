# Generated by Django 3.2.7 on 2021-10-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20211024_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AddField(
            model_name='cost',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий рекрутера'),
        ),
    ]
