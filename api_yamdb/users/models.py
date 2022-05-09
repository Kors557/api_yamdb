from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # role = ?
    username = models.CharField(
        "Имя пользователя",
        max_length=150,
        unique=True,
        blank=False,
        null=False,
    )
    bio = models.TextField('Биография', blank=True,)
    email = models.EmailField("email", unique=True, null=False, max_length=254)
    first_name = models.CharField("Имя", max_length=150, blank=True)
    last_name = models.CharField("Фамилия", max_length=150, blank=True)
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=155,
        null=True
    )
