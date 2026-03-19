from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio para crear usuarios.')
        return super()._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()