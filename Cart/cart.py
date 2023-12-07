from django.contrib.auth.models import User
from SeniorProjectApp.models import UserCart, CartItem

class Cart():
    def __init__(self, request):
        self.request = request 

        if request.user.is_authenticated:
            user_id = str(request.user.id)
            cart = self.request.session.get(user_id, {})
        else:
            cart = self.request.session.get('guest_cart', {})
        
        self.cart = cart

    def add(self, item):
        item_id = str(item.id)

        if item_id in self.cart:
            self.cart[item_id]['quantity'] += 1
        else:
            self.cart[item_id] = {
                'name': item.name,
                'price': str(item.price),
                'quantity': 1,
                'id': item.id
            }

        if self.request.user.is_authenticated:
            user_id = str(self.request.user.id)
            self.request.session[user_id] = self.cart
        else:
            self.request.session['guest_cart'] = self.cart

        self.request.session.modified = True
 
    def remove(self, item):
        item_id = str(item.id)

        if item_id in self.cart:
            self.cart[item_id]['quantity'] -= 1
            if self.cart[item_id]['quantity'] == 0:
                del self.cart[item_id]

            if self.request.user.is_authenticated:
                user_id = str(self.request.user.id)
                self.request.session[user_id] = self.cart

                user_cart, _ = UserCart.objects.get_or_create(user=self.request.user)
                cart_item = CartItem.objects.get(product=item, cart=user_cart)

                # Check if the quantity is greater than 1, then decrement the quantity
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                    cart_item.save()
                else:
                    # If the quantity is 1, remove the entire CartItem
                    cart_item.delete()

                # Remove the cart item from the UserCart
                user_cart.products.remove(item)
            else:
                self.request.session['guest_cart'] = self.cart

            self.request.session.modified = True


    def __len__(self):
        return len(self.cart)