from django.shortcuts import get_object_or_404, render, redirect
from .models import MenuItemCategory, MenuItem, Menu, Order, Carausel
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


# Create your views here.

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

