# Generated by Django 3.2.7 on 2022-08-29 20:24

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0044_remove_group_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='material',
            field=models.FileField(blank=True, null=True, upload_to=mainapp.models.get_file_path, verbose_name='Материал'),
        ),
    ]
