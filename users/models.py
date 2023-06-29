from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=50)
    img = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return f"Username: {self.username}"
