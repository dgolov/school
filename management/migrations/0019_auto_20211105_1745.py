# Generated by Django 3.2.7 on 2021-11-05 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.staff', verbose_name='HR'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий менеджера'),
        ),
    ]
