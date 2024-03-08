from django.urls import path
from . import views

app_name = 'homepages'

urlpatterns = [
    path('', views.index, name="index"),
    path('single/<int:product_id>', views.single, name="single"),
    path('collections/<str:category_name>', views.collections, name="collections"),
    path('cart', views.cart, name="cart"),
    path('add_cart/<int:product_id>', views.add_cart, name="add_cart"),
    path('logout', views.logout_view, name="logout_view"),
    path('remove_cart_item/<str:key>', views.remove_cart_item, name="remove_cart_item"),
    path('update_total/<str:key>', views.update_total, name="update_total")
]
