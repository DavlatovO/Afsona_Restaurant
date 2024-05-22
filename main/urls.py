from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('register/',views.register,name='register'),
    path('about/',views.register,name='about'),
    path('booking/',views.booking,name='booking'),
    path('menu/',views.menu, name='menu'),
    path('dish-detail/<slug:slug>/', views.dish_detail, name='dish_detail'),
    path('add_to_cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_cart', views.update_cart, name='update_cart'),


]