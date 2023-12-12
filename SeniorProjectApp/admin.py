from django.contrib import admin
from .models import MenuItemCategory, MenuItem, Menu, Carausel, UserCart, CartItem

admin.site.register(MenuItem)
admin.site.register(MenuItemCategory)
admin.site.register(Menu)
admin.site.register(Carausel)

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class UserCartAdmin(admin.ModelAdmin):
    list_display = ['user']
    inlines = [CartItemInline]

admin.site.register(UserCart, UserCartAdmin)
admin.site.register(CartItem)