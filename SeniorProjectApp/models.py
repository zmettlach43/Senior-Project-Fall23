from django.db import models

# Create your models here.

class MenuItemCategory(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
   name = models.CharField(max_length=100)
   addin = models.CharField(max_length=100, blank=True)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   category = models.ForeignKey(MenuItemCategory, on_delete=models.CASCADE)

   def __str__(self):
       return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.name