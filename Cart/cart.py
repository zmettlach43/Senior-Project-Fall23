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

        
    def __len__(self):
        return len(self.cart)