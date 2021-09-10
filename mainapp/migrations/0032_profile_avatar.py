# Generated by Django 3.2.7 on 2021-09-10 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0031_auto_20210910_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='mainapp.photo', verbose_name='Аватарка'),
        ),
    ]
