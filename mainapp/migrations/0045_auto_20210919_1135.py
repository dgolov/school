# Generated by Django 3.2.7 on 2021-09-19 11:35

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0044_alter_lesson_video_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicperformance',
            name='classwork_grade',
        ),
        migrations.RemoveField(
            model_name='academicperformance',
            name='examination_grade',
        ),
        migrations.RemoveField(
            model_name='academicperformance',
            name='homework_grade',
        ),
        migrations.RemoveField(
            model_name='academicperformance',
            name='test_grade',
        ),
        migrations.AddField(
            model_name='academicperformance',
            name='grade',
            field=mainapp.models.IntegerRangeField(default=10, verbose_name='Оценка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='academicperformance',
            name='type_grade',
            field=models.CharField(choices=[('homework', 'Домашняя работа'), ('classwork', 'Класная работа'), ('test', 'Контрольная работа'), ('examination', 'Экзамен')], default='homework', max_length=50, verbose_name='Тип оценки'),
            preserve_default=False,
        ),
    ]
