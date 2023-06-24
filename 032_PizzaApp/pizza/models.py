from django.db import models
from django.contrib.auth.models import User


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=64)
    toppings = models.ManyToManyField(Topping)
    image = models.ImageField(upload_to='pizza_pics', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, choices=SIZES, default="M")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} # {self.pizza.name} * {self.quantity} "
