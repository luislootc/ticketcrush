from secrets import choice
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, Permission
from applications.users.managers import UserManager


class User(AbstractBaseUser, Permission):

    GENDER_CHOICES = (
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro')
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = 'Usuarios'
        unique_together = ('email','username')
