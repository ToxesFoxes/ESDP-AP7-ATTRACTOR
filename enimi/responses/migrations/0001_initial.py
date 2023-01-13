# Generated by Django 4.1.4 on 2023-01-13 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cabinet_parents", "0011_alter_survey_student_area_alter_survey_tutor_area"),
    ]

    operations = [
        migrations.CreateModel(
            name="Response",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hello_message",
                    models.TextField(
                        blank=True,
                        default="Здравствуйте. Меня заинтересовала ваша анкета!",
                        max_length=3000,
                        verbose_name="Приветственное сообщение",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Удалено"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "changed_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата изменения"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responses",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор отклика",
                    ),
                ),
                (
                    "subjects",
                    models.ManyToManyField(
                        related_name="responses",
                        to="cabinet_parents.subject",
                        verbose_name="Предметы",
                    ),
                ),
                (
                    "survey",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responses",
                        to="cabinet_parents.survey",
                        verbose_name="Анкета",
                    ),
                ),
            ],
        ),
    ]
