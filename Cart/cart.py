from django.contrib.auth.models import User

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
            del self.cart[item_id]
            
            if self.request.user.is_authenticated:
                user_id = str(self.request.user.id)
                self.request.session[user_id] = self.cart
            else:
                self.request.session['guest_cart'] = self.cart

            self.request.session.modified = True

    def __len__(self):
        return len(self.cart)