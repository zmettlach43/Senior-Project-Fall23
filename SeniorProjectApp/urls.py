from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('cart', views.cart, name="cart"),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
]