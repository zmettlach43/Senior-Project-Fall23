from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name="register"),
    
]