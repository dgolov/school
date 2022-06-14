# Generated by Django 3.2.7 on 2022-06-08 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0040_auto_20220511_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': '06. Города',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='news',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.city', verbose_name='Город'),
        ),
    ]
