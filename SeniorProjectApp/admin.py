from django.contrib import admin
from .models import MenuItemCategory, MenuItem, Menu, Carausel, UserCart, CartItem
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(MenuItemCategory)
admin.site.register(Menu)
admin.site.register(Carausel)
admin.site.register(UserCart)
admin.site.register(CartItem)