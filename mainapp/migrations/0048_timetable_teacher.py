# Generated by Django 3.2.7 on 2022-09-15 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0047_auto_20220914_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.teacher', verbose_name='Преподаватель'),
        ),
    ]
