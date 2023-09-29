from django.db import models

# Create your models here.

class MenuItemCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
   name = models.CharField(max_length=100)
   descritpion = models.TextField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   category = models.ForeignKey(MenuItemCategory, on_delete=models.CASCADE)

   def __str__(self):
       return self.name + " " + self.price

class Menu(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.name