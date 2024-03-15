from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', next_page="homepages:index"), name="login"),
    path('logout/', LogoutView.as_view(next_page="homepages:index"), name="logout_view"),
    path('register/', views.register, name="register"),
]