from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import product, discount

# Create your views here.
def index(request):
    products = product.objects.all().order_by('-modified_at')[:10]

    context = {'products' : products}
    
    return render(request, 'index.html', context)