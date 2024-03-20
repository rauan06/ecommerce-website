from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', next_page="homepages:index", redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(next_page="homepages:index"), name="logout_view"),
    path('register/', views.register, name="register"),
    path('checkout/', views.checkout, name="checkout"),
    path('orders/', views.orders, name="orders")
]