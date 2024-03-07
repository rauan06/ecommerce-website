from django.urls import path
from . import views

app_name = 'homepages'

urlpatterns = [
    path('', views.index, name="index"),
    path('single/<int:product_id>', views.single, name="single"),
    path('collections/<str:category_name>', views.collections, name="collections"),
    path('cart', views.cart, name="cart"),
    path('add_cart', views.add_cart, name="add_cart"),
]
