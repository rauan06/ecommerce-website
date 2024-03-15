from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            instance = form.save() #form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            instance.email = email
            instance.first_name = first_name
            instance.last_name = last_name
            instance.save()
            form.save_m2m()
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    else: form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)