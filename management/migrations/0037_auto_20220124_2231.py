# Generated by Django 3.2.7 on 2022-01-24 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_category_how_is_the_training'),
        ('management', '0036_merge_0034_auto_20220116_1649_0035_auto_20220109_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_email',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Email из заявки'),
        ),
        migrations.AddField(
            model_name='request',
            name='request_fio',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ФИО из заявки'),
        ),
        migrations.AddField(
            model_name='request',
            name='request_phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон из заявки'),
        ),
        migrations.AddField(
            model_name='request',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.student', verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='request',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.client', verbose_name='Клиент'),
        ),
    ]
