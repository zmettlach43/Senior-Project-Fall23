from django.shortcuts import render
from .models import MenuItemCategory, MenuItem, Menu, Cart

# Create your views here.

def home(request):
    return render(request, "SeniorProjectApp/home.html")

def menu(request):
    categories = MenuItemCategory.objects.all()
    return render(request, "SeniorProjectApp/menu.html", {'categories': categories})

def aboutus(request):
    return render(request, "SeniorProjectApp/aboutus.html", {})

def cart(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        cart_obj = Cart.objects.create(user=None)
        request.session['cart_id'] = 12
        print('New Cart created')
    else:
        print('Cart ID exists')
        print(cart_id)
        cart_obj = Cart.objects.create(id=cart_id)
    return render(request, "SeniorProjectApp/cart.html", {})

