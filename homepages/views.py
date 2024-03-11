from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import product, product_category
from .forms import Cart
from django.contrib.auth import logout


# Create your views here.
def logout_view(request):
    """Deletes all sessions"""
    logout(request)
    return HttpResponseRedirect(reverse('homepages:cart'))

def index(request):
    """Shows last 10 modified products """
    products = product.objects.all().order_by('-modified_at')[:10]

    context = {'products' : products}
    
    return render(request, 'index.html', context)


def single(request, product_id):
    """Single page with simple form"""
    item = product.objects.get(id=product_id)
    form = Cart()
    
    context = {'product':  item, 'form': form}

    return render(request, 'single.html', context)


def collections(request, category_name):
    """Show items according to the category"""
    items = product_category.objects.get(name = category_name).product_set.all()

    context = {'products' : items.order_by('-modified_at'), 'title' : category_name}

    return render(request, 'collections.html', context)


def cart(request):
    """Gets the values from request.session['cart_items'], and gives it to the cart page""" 
    if 'cart_items' in request.session:
        total = 0
        
        for values in request.session['cart_items']:
            if request.session['cart_items'][values]['discount_active']:
                total += int(request.session['cart_items'][values]['quantity']) * (int(request.session['cart_items'][values]['price']) - int(request.session['cart_items'][values]['price']) * int(request.session['cart_items'][values]['discount']) / 100)
            else:
                total += int(request.session['cart_items'][values]['quantity']) * int(request.session['cart_items'][values]['price'])
        return render(request, 'cart.html', {'cart_items':request.session['cart_items'], 'total' : total})
    return render(request, 'cart.html', {'cart_items':''})


def add_cart(request, product_id):
    """Adds items to request.session['cart_items'], in fact, this is our cart"""
    item = get_object_or_404(product, id=product_id)

    if request.method != 'GET':
        form = Cart()
    else:
        form = Cart(request.GET)
        if form.is_valid():
            cart_items = request.session.get('cart_items', {})  # Get cart_items from session or create an empty dict
            if str(product_id)  + request.GET['sizes'] in cart_items:
                cart_items[str(product_id)  + request.GET['sizes']]['quantity'] += int(request.GET['quantity'])
                request.session['quantity'] += int(request.GET['quantity'])
            else:
                cart_items[str(product_id)  + request.GET['sizes']] = { # Creating 2 dimensional array with index [product_id + size]
                    'id': product_id,
                    'name': item.name,
                    'image': str(item.image),
                    'price': item.price,
                    'discount': int(item.discount.discount_percent),
                    'discount_active': item.discount.active,
                    'size': request.GET['sizes'],
                    'quantity': int(request.GET['quantity']),
                }
                request.session['quantity'] = int(request.GET['quantity'])
            request.session['cart_items'] = cart_items  # Update cart_items in session
            return HttpResponseRedirect(reverse('homepages:cart'))

    context = {'product': item, 'form': form}
    return render(request, 'single.html', context)


def remove_cart_item(request, key):
    """Handling excepetions"""
    if 'cart_items' in request.session and key in request.session['cart_items']:
        request.session['quantity'] -= request.session['cart_items'][key]['quantity']
        del request.session['cart_items'][key]
        request.session.modified = True
        return render(request, 'cart.html', {'cart_items': request.session['cart_items']})
    else:
        if 'cart_items' in request.session:
            return render(request, 'cart.html', {'cart_items': request.session['cart_items']})
        else:
            return render(request, 'cart.html', {'cart_items': ''})


def update_total(request, key):
    """Handling excepetions"""

    if request.method != 'GET':
        return render(request, 'cart.html')
    else:
            try:
                if 'cart_items' in request.session and key in request.session['cart_items']:
                    request.session['quantity'] -= int(request.session['cart_items'][key]['quantity'])
                    request.session['cart_items'][key]['quantity'] = int(request.GET['quantity'])
                    request.session['quantity'] += abs(int(request.GET['quantity']))
                    request.session.modified = True
                    
                total = 0
                for values in request.session['cart_items']:
                    if request.session['cart_items'][values]['discount_active']:
                        total += int(request.session['cart_items'][values]['quantity']) * (int(request.session['cart_items'][values]['price']) - int(request.session['cart_items'][values]['price']) * int(request.session['cart_items'][values]['discount']) / 100)
                    else:
                        total += int(request.session['cart_items'][values]['quantity']) * int(request.session['cart_items'][values]['price'])

                return render(request, 'cart.html', {'cart_items':request.session['cart_items'], 'total' : total})
            
            except KeyError:
                Http404