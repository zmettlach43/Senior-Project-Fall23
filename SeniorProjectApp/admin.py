from django.contrib import admin
from .models import MenuItemCategory, MenuItem, Menu, Customer, Carausel, Order

# Register your models here.

admin.site.register(MenuItem)
admin.site.register(MenuItemCategory)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Carausel)
admin.site.register(Order)