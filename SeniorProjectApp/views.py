from django.shortcuts import get_object_or_404, render, redirect
from .models import MenuItemCategory, MenuItem, Menu, Order, Carausel
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    return render(request, 'SeniorProjectApp/index.html', {'user': request.user})

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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("Credential are incorrect... Please Try again"))
            return redirect('login')

    else:
        return render(request, "SeniorProjectApp/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out.'))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Your Account Has Been Created!'))
            return redirect('home')
        else:
            messages.success(request, ('There was a problem making your account. Please try again '))
            return redirect('register')
    else: 
        return render(request, "SeniorProjectApp/register.html", {'form': form})
    
    stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    try:
        # Create a new Stripe Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Product Name',
                        # Add more product details if necessary
                    },
                    'unit_amount': 1000,  # Price in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),  # Update the URL to your success route
            cancel_url=request.build_absolute_uri('/cancel/'),    # Update the URL to your cancel route
        )


        # Redirect the user to Stripe Checkout
        return redirect(checkout_session.url, code=303)

    except Exception as e:
        return render(request, 'SeniorProjectApp/checkout.html', {'error': str(e)})
    
    # Other imports and view functions...

def payment_success(request):
    # Handle the successful payment scenario
    # You can add logic here to update order status, send confirmation emails, etc.
    return render(request, 'SeniorProjectApp/payment_success.html', {})

def payment_cancel(request):
    # Handle the payment cancellation scenario
    return render(request, 'SeniorProjectApp/payment_cancel.html', {})


# Other view functions...