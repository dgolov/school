# Generated by Django 3.2.7 on 2021-11-05 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_auto_20211105_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.staff', verbose_name='Менеджер клиента'),
        ),
        migrations.AlterField(
            model_name='request',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.staff', verbose_name='Менеджер'),
        ),
    ]