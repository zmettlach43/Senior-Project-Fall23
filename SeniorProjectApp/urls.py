from django.conf import settings
from django.conf.urls.static import static
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
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                        document_root = settings.MEDIA_ROOT)

