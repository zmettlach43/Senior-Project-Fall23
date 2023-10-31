from django.contrib import admin
from .models import MenuItemCategory, MenuItem, Menu, Cart, Carausel

# Register your models here.

admin.site.register(MenuItem)
admin.site.register(MenuItemCategory)
admin.site.register(Menu)
admin.site.register(Cart)
admin.site.register(Carausel)