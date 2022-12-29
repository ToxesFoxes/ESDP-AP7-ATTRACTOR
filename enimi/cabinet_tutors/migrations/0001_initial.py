# Generated by Django 4.1.4 on 2022-12-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.CharField(blank=True, max_length=50, null=True, verbose_name='Дата рождения')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Мужчина'), ('female', 'Женщина')], default='male', max_length=150, null=True, verbose_name='Пол')),
                ('language', models.CharField(blank=True, choices=[('kazakh', 'Казахский'), ('russian', 'Русский'), ('english', 'Английский')], default='kazakh', max_length=150, null=True, verbose_name='Язык преподавания')),
                ('about_me', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Коротко о себе')),
            ],
        ),
        migrations.CreateModel(
            name='StudyFormats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectsAndCosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TutorEducationAndDiplomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
