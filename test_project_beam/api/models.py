from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField('username', max_length=100, unique=True)
    email = models.EmailField('email', unique=True, null=True, blank=True)
    age = models.PositiveIntegerField('age', null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar',upload_to='avatars/')
    bio = models.TextField('bio')

    def __str__(self):
        return f"Profile of {self.user.name}"

class Product(models.Model):
    name = models.CharField('product name',max_length=100)
    price = models.DecimalField('Price',max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField('total_price',max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order by {self.user.name}"


