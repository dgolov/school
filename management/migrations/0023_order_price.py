# Generated by Django 3.2.7 on 2021-11-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_alter_request_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=30000, verbose_name='Оплаченная сумма'),
            preserve_default=False,
        ),
    ]
