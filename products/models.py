from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.upper()


class Product(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10000000, decimal_places=2)
    address = models.CharField(max_length=300)
    number = models.CharField(max_length=15)
    telegram = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment of {self.author.username}"
