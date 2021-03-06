# Generated by Django 3.2.7 on 2022-01-16 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_alter_eventday_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='skills',
        ),
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание'),
        ),
        migrations.AddField(
            model_name='skill',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.course', verbose_name='Курс'),
            preserve_default=False,
        ),
    ]
