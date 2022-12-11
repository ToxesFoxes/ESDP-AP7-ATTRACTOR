from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import UserManager


class UserCategoryChoices(TextChoices):
    STUDY_CENTER = 'study_center', 'Учебный центр'
    STUDENT = 'student', 'Ученик'
    TUTOR = 'tutor', 'Репетитор'
    PARENTS = 'parents', 'Родители'


class Account(AbstractUser):
    type = models.CharField(
        verbose_name='Тип пользователя',
        choices=UserCategoryChoices.choices,
        max_length=200,
        null=False,
        blank=False,
    )
    father_name = models.CharField(
        verbose_name='Отчество',
        max_length=200,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False
    )
    phone = PhoneNumberField(
        unique=True,
        null=False,
        blank=False
    )
    avatar = models.ImageField(
        null=False,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар',
        default='default_avatar/default-user.png'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'
