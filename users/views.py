from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required
def checkout(request):
    if 'cart_items' in request.session:
        total = 0
        
        for values in request.session['cart_items']:
            # Calculate total price considering discounts
            if request.session['cart_items'][values]['discount_active']:
                # Round down the price to the nearest multiple of 10
                rounded_price = round(round(request.session['cart_items'][values]['price'], -1) 
                             - round(request.session['cart_items'][values]['price'], -1) 
                              * request.session['cart_items'][values]['discount'] / 100, -1) 
                # Calculate the total with the rounded price
                total += int(int(request.session['cart_items'][values]['quantity']) * rounded_price )
            else:
                total += int(request.session['cart_items'][values]['quantity']) * \
                int(request.session['cart_items'][values]['price'])
        print(request.session['cart_items'])       
        return render(request, 'checkout.html', {'cart_items': request.session['cart_items'], 'total': total})
    raise Http404


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("homepages:index"))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            return HttpResponseRedirect(reverse('homepages:index'))
    else: form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)