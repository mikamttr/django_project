from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    EMPLOYER = 'EMPLOYER'
    MANAGER = 'MANAGER'

    ROLE_CHOICES = (
        (EMPLOYER, 'employer'),
        (MANAGER, 'manager'),
    )
    user_role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
