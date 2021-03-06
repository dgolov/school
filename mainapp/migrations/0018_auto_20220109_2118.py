# Generated by Django 3.2.7 on 2022-01-09 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20220109_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='program',
        ),
        migrations.RemoveField(
            model_name='eventday',
            name='name',
        ),
        migrations.AddField(
            model_name='eventday',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.event', verbose_name='Мероприятие'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventday',
            name='number',
            field=models.IntegerField(default=1, verbose_name='День мероприятия'),
            preserve_default=False,
        ),
    ]
