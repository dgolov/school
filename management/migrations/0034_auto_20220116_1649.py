# Generated by Django 3.2.7 on 2022-01-16 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0033_advertisingactivity_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_status',
            field=models.CharField(blank=True, choices=[('contract', 'Заключен договор'), ('meeting', 'Назначена встреча'), ('waiting_call', 'Ждет звонка'), ('will_think', 'Будет думать'), ('refusal', 'Отказ'), ('dissatisfied', 'Недовольный клиент'), ('no_connection', 'Нет ответа')], max_length=50, null=True, verbose_name='Последний статус по заявкам'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_contract', to='management.client', verbose_name='Клиент'),
        ),
    ]
