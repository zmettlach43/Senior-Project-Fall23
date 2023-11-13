from django.db import models
from django.conf import settings
from django import forms
import datetime

User = settings.AUTH_USER_MODEL

# Create your models here.

class MenuItem(models.Model):
   name = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   image = models.ImageField(upload_to='uploads/menuitems/', default='static/default_image.png')

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
    image = models.ImageField(upload_to= '')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

#Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
#Customer Order
class Order(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.item
