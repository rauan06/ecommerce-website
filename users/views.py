from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    
    return render(request, 'login.html')

def logout_view(requset):
    logout(requset)
    return render(requset, "homepages/templates/index.hmtl")

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display registration form
        form = UserCreationForm()
    else:
        """Form was filled"""
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and rediret to home page
            auth_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, auth_user)
            return HttpResponseRedirect(reverse('homepages:index'))

    context = {'form' : form}
    return render(request, 'register.html', context)
