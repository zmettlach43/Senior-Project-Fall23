from django.shortcuts import render, get_object_or_404
from .cart import Cart
from SeniorProjectApp.models import MenuItem, UserCart, CartItem
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser

def cart(request):
    if request.user.is_authenticated:
        cart, created = UserCart.objects.get_or_create(user=request.user)
        name = cart.cartitem_set.first().product.name if cart.cartitem_set.exists() else None
        cart_items = cart.cartitem_set.all()
        total_price = sum(float(cart_item.product.price) * cart_item.quantity for cart_item in cart_items)
    else:
        cart_items = []
        total_price = 0
        name = None

    return render(request, "cart/cart.html", {'cart_items': cart_items, 'total_price': total_price, 'name': name})


def cart_add(request):
    # Create a Cart object to manage the cart
    cart = Cart(request)

    # Check if the request is a POST request with the 'action' parameter set to 'post'
    if request.POST.get('action') == 'post':
        # Get the item ID from the request
        item_id = int(request.POST.get('product_id'))
        # Get the MenuItem object corresponding to the item ID
        item = get_object_or_404(MenuItem, id=item_id)

        # Check if the item is already in the user's cart
        if request.user.is_authenticated:
            # If the user is authenticated, get or create their cart
            user_cart, created = UserCart.objects.get_or_create(user=request.user)
            cart_item, cart_item_created = CartItem.objects.get_or_create(product=item, cart=user_cart)

            # If the item already exists in the cart, increment the quantity
            if not cart_item_created:
                cart_item.quantity += 1
                cart_item.save()
        else:
            # If the user is not authenticated, allow adding items to the cart without creating a UserCart
            cart.add(item, quantity=1)

        # Get the current cart quantity
        cart_quantity = len(cart)

        # Prepare the response data with the updated cart quantity
        response_data = {'qty': cart_quantity}
        return JsonResponse(response_data)

    # If the request does not have the 'action' parameter or is not 'post', return an error response
    response_data = {'message': 'Invalid request.'}
    return JsonResponse(response_data, status=400)


def cart_delete(request):
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('product_id'))
        user_cart = get_object_or_404(UserCart, user=request.user)
        
        # Retrieve all instances of the item in the user's cart
        cart_items = CartItem.objects.filter(product__id=item_id, cart=user_cart)
        
        # Delete one instance of the item (if it exists)
        if cart_items.exists():
            # Decrease the quantity by 1, and save the instance
            cart_item = cart_items.first()
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                # If the quantity is 1, remove the entire instance
                cart_item.delete()

        cart_quantity = len(Cart(request))
        response_data = {'qty': cart_quantity}
        return JsonResponse(response_data)