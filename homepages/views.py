from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import product, product_category
from .forms import Cart

# Create your views here.
def index(request):
    products = product.objects.all().order_by('-modified_at')[:10]

    context = {'products' : products}
    
    return render(request, 'index.html', context)


def single(request, product_id):
    item = get_object_or_404(product, id=product_id)
    form = Cart()
    
    context = {'product' : item, 'form' : form}

    return render(request, 'single.html', context)


def collections(request, category_name):
    items = product_category.objects.get(name = category_name).product_set.all()

    context = {'products' : items.order_by('-modified_at'), 'title' : category_name}

    return render(request, 'collections.html', context)


def cart(request):
    context = {'cart_items' : request.session['cart_items']} 

    return render(request, 'cart.html', context)


def add_cart(request):
    request.session['cart_items'] = {
        'name':'',
        'price':'',
        'quantity':''
    }

    