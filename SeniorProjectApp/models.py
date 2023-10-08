from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MenuItem(models.Model):
   name = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=10, decimal_places=2)

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