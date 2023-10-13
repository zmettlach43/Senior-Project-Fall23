from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

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
    
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(MenuItem, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.id)