from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required
def checkout(request):
    """Function for checkout"""
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
    
    # User entered the url directly
    raise Http404


def register(request):
    """Function for creating a user and authenticating"""
    if request.user.is_authenticated:
        # Redirect user to the homepage if user is already registered
        return HttpResponseRedirect(reverse("homepages:index"))
    
    if request.method == 'POST':
        # User sent the form
        form = UserCreationForm(request.POST)
        
        # User filled the fields correctly 
        if form.is_valid():
            # User is saved in the database
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Authericating the user, so the user doesn't have to login after reg.
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            return HttpResponseRedirect(reverse('homepages:index'))
    
    # User just opened the page, send the reg. form structure 
    else: form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def orders(request):
    """Functions to show the user's orders"""
    return render(request, 'order.html')