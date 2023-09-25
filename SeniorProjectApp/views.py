from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "SeniorProjectApp/home.html")

def menu(request):
    return render(request, "SeniorProjectApp/menu.html", {})

def aboutus(request):
    return render(request, "SeniorProjectApp/aboutus.html", {})

def checkout(request):
    return render(request, "SeniorProjectApp/checkout.html", {})