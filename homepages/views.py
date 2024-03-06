from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import product, discount

# Create your views here.
def index(request):
    products = product.objects.all().order_by('-modified_at')[:10]

    context = {'products' : products}
    
    return render(request, 'index.html', context)


def single(request, product_id):
    item = get_object_or_404(product, id=product_id)
    
    context = {'product' : item}

    return render(request, 'single.html', context)