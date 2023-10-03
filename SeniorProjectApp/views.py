from django.shortcuts import render
from .models import MenuItemCategory, MenuItem, Menu

# Create your views here.

def home(request):
    return render(request, "SeniorProjectApp/home.html")

def menu(request):
    menuitems = MenuItem.objects.all().values()
    return render(request, "SeniorProjectApp/menu.html", {'menuitems': menuitems})

def aboutus(request):
    return render(request, "SeniorProjectApp/aboutus.html", {})

def checkout(request):
    return render(request, "SeniorProjectApp/checkout.html", {})