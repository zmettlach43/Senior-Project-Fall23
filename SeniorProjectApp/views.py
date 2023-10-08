from django.shortcuts import render, redirect
from .models import MenuItemCategory, MenuItem, Menu

# Create your views here.

def home(request):
    return render(request, "SeniorProjectApp/home.html")

def menu(request):
    categories = MenuItemCategory.objects.all()
    return render(request, "SeniorProjectApp/menu.html", {'categories': categories})

def aboutus(request):
    return render(request, "SeniorProjectApp/aboutus.html", {})

def checkout(request):
    return render(request, "SeniorProjectApp/checkout.html", {})

