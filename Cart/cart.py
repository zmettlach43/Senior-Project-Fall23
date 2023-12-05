class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
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

        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)

        if item_id in self.cart:
            del self.cart[item_id]
            self.session.modified = True

    def __len__(self):
        return len(self.cart)