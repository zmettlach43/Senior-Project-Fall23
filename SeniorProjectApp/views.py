from django.shortcuts import get_object_or_404, render
from .models import MenuItemCategory, MenuItem, Menu, Cart, Carausel

# Create your views here.

def home(request):
    obj = Carausel.objects.all()
    context = {
        'obj':obj
    }

    return render(request, "SeniorProjectApp/home.html", context)

def menu(request):
    categories = MenuItemCategory.objects.all()
    return render(request, "SeniorProjectApp/menu.html", {'categories': categories})

def item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'SeniorProjectApp/item_detail.html/', {'item': item})

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

