from django.db import models
from django.conf import settings
from django import forms
from django.contrib.auth.models import User
import datetime

User = settings.AUTH_USER_MODEL

# Create your models here.

class MenuItem(models.Model):
   name = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   image = models.ImageField(upload_to='uploads/menuitems/', default='static/default_image.png')
   description = models.TextField(max_length=500, blank=True)  # New field for description


   def __str__(self):
       return self.name
   
class MenuItemCategory(models.Model):
    name = models.CharField(max_length=100)
    menu_items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(MenuItemCategory)

    def __str__(self):
        return self.name

class Carausel(models.Model):
    image = models.ImageField(upload_to= 'uploads/carausel/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(MenuItem, through='CartItem')

class CartItem(models.Model):
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)