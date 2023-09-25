from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('checkout', views.checkout, name="checkout"),
]