from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=50, unique=True)
    img = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return f"Username: {self.username}"


class Saved(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment of {self.author.username}"
