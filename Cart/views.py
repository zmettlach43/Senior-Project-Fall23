from django.shortcuts import render, get_object_or_404
from .cart import Cart
from SeniorProjectApp.models import MenuItem, UserCart, CartItem
from django.http import JsonResponse

def cart(request):
    cart, created = UserCart.objects.get_or_create(user=request.user)
    
    name = cart.cartitem_set.first().product.name if cart.cartitem_set.exists() else None
    cart_items = cart.cartitem_set.all()
    total_price = sum(float(cart_item.product.price) * cart_item.quantity for cart_item in cart_items)

    return render(request, "cart/cart.html", {'cart_items': cart_items, 'total_price': total_price, 'name': name})



def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('product_id'))
        item = get_object_or_404(MenuItem, id=item_id)

        user_cart, created = UserCart.objects.get_or_create(user=request.user)

        # Check if the item is already in the user's cart
        cart_item, cart_item_created = CartItem.objects.get_or_create(product=item, cart=user_cart)

        # If the item already exists in the cart, increment the quantity
        if not cart_item_created:
            cart_item.quantity += 1
            cart_item.save()

        cart_quantity = len(cart)

        response_data = {'qty': cart_quantity}
        return JsonResponse(response_data)


def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('product_id'))
        item = get_object_or_404(MenuItem, id=item_id)

        cart.remove(item)
        cart_quantity = len(cart)

        response_data = {'qty': cart_quantity, 'message': f'Item {item_id} removed successfully.'}
        return JsonResponse(response_data)



