from django.shortcuts import render, get_object_or_404
from .cart import Cart
from SeniorProjectApp.models import MenuItem
from django.http import JsonResponse

def cart(request):
    cart = Cart(request)
    cart_items = cart.cart.values()
    name = cart.cart.values
    total_price = sum(float(item['price']) for item in cart_items)

    return render(request, "cart/cart.html", {'cart_items': cart_items, 'total_price': total_price, 'name': name})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('product_id'))
        item = get_object_or_404(MenuItem, id=item_id)

        cart.add(item=item)
        cart_quantity = cart.__len__()

        response_data = {'qty': cart_quantity}
        return JsonResponse(response_data)


def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('product_id'))
        item = get_object_or_404(MenuItem, id=item_id)

        cart.remove(item)
        cart_quantity = len(cart)

        response_data = {'qty': cart_quantity}
        return JsonResponse(response_data)

def cart_update(request):
    pass


