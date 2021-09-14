from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    role = models.CharField(default=UserRole.USER, max_length=35,
                            choices=UserRole.choices)
    bio = models.TextField(blank=True, null=True, max_length=500)
    confimation_code = models.CharField(max_length=10,
                                        unique=True,
                                        null='True')

    @property
    def is_admin(self):
        return self.is_staff or self.role == UserRole.ADMIN

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.email
