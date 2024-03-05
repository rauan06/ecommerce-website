from django.urls import path
from . import views

app_name = 'homepages'

urlpatterns = [
    path('', views.index, name="index")
]
