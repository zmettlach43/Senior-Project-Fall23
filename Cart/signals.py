from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import UserCart

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # Retrieve or create the user's cart
    cart, created = UserCart.objects.get_or_create(user=user)

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    # Save the user's cart state
    # You may want to add additional logic, like merging guest cart items with the user's cart
    cart = UserCart.objects.get(user=user)
    # Save the cart state
    cart.save()
