# Generated by Django 3.2.7 on 2022-02-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_course_in_main_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='in_main_page',
            field=models.BooleanField(default=False, verbose_name='На главной странице'),
        ),
    ]
