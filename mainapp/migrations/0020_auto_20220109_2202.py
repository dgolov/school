# Generated by Django 3.2.7 on 2022-01-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_student_verification'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAgeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.CharField(choices=[('children', 'Дети'), ('teens', 'Подростки'), ('adults', 'Взрослые')], max_length=50, verbose_name='Возрастная категория')),
            ],
            options={
                'verbose_name': 'Возрастные группы студентов',
                'verbose_name_plural': '01. Пользователи - Возрастные группы',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='age_group_access',
            field=models.ManyToManyField(blank=True, related_name='student_age_group_access', to='mainapp.StudentAgeGroup', verbose_name='Доступы по возрастным категориям'),
        ),
    ]
