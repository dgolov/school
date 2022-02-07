# Generated by Django 3.2.7 on 2022-01-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0037_auto_20220124_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='purpose',
            field=models.CharField(blank=True, choices=[('price', 'Узнать цену'), ('meeting', 'Договориться о встрече'), ('info', 'Получить общую информацию'), ('details', 'Уточнить детали перед заключением договора'), ('repeat', 'Повторная консультация'), ('free_lesson', 'Записаться на пробный урок')], max_length=50, null=True, verbose_name='Цель заявки'),
        ),
    ]