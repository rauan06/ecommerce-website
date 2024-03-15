from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import product, product_category
from .forms import Cart
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout

# Create your views here.

def index(request):
    """Shows last 10 modified products"""
    products = product.objects.all().order_by('-modified_at')[:10]

    context = {'products' : products}
    
    return render(request, 'index.html', context)


def single(request, product_id):
    """Renders a single page with a simple form for a specific product"""
    item = product.objects.get(id=product_id)
    form = Cart()
    
    context = {'product':  item, 'form': form}

    return render(request, 'single.html', context)


def collections(request, category_name):
    """Shows items according to the category"""
    items = product_category.objects.get(name=category_name).product_set.all()

    context = {'products': items.order_by('-modified_at'), 'title': category_name}

    return render(request, 'collections.html', context)

@login_required
def cart(request):
    """Displays the items stored in the cart session"""
    if 'cart_items' in request.session:
        total = 0
        
        for values in request.session['cart_items']:
            # Calculate total price considering discounts
            if request.session['cart_items'][values]['discount_active']:
                total += int((int(request.session['cart_items'][values]['quantity']) * \
                       (int(request.session['cart_items'][values]['price']) 
                       -int(request.session['cart_items'][values]['price']) * \
                        int(request.session['cart_items'][values]['discount']) / 100))/10)*10
            else:
                total += int(request.session['cart_items'][values]['quantity']) * \
                         int(request.session['cart_items'][values]['price'])
        return render(request, 'cart.html', {'cart_items': request.session['cart_items'], 'total': total})
    return render(request, 'cart.html', {'cart_items': ''})


@login_required
def add_cart(request, product_id):
    """Adds items to the cart session"""
    item = get_object_or_404(product, id=product_id)
    if 'quantity' not in request.session:
        request.session['quantity'] = 0

    if request.method != 'GET':
        form = Cart()
    else:
        form = Cart(request.GET)
        if form.is_valid():
            cart_items = request.session.get('cart_items', {})  
            # Get cart_items from session or create an empty dict
            if str(product_id) + request.GET['sizes'] in cart_items:
                # If the same product in the same size is added again, increase its quantity
                cart_items[str(product_id) + request.GET['sizes']]['quantity'] += int(request.GET['quantity'])
                request.session['quantity'] += int(request.GET['quantity'])
            else:
                # Create a new entry in cart_items for the product
                cart_items[str(product_id) + request.GET['sizes']] = {
                    'id': product_id,
                    'name': item.name,
                    'image': str(item.image),
                    'price': item.price,
                    'discount': int(item.discount.discount_percent),
                    'discount_active': item.discount.active,
                    'size': request.GET['sizes'],
                    'quantity': int(request.GET['quantity']),
                    # 'update_total' : UpdateTotal(),
                }
                request.session['quantity'] += int(request.GET['quantity'])
            request.session['cart_items'] = cart_items  # Update cart_items in session
            return HttpResponseRedirect(reverse('homepages:cart'))

    context = {'product': item, 'form': form}
    return render(request, 'single.html', context)

@login_required
def remove_cart_item(request, key):
    """Removes an item from the cart session"""
    # Check if the key is in the request session
    if 'cart_items' in request.session and key in request.session['cart_items']:
        request.session['quantity'] -= request.session['cart_items'][key]['quantity']
        del request.session['cart_items'][key]
        request.session.modified = True
        return HttpResponseRedirect(reverse('homepages:update_total', args=[key]))
    # Else return cart without any changes
    else:
        # Check if the cart had items or not 
        if 'cart_items' in request.session:
            return HttpResponseRedirect(reverse('homepages:update_total', args=[key]))
        else:
            return render(request, 'cart.html', {'cart_items': ''})

@login_required
def update_total(request, key):
    """Updates the total price of the cart"""
    try:
        if int(request.GET.get('quantity', 1)) == 0:
            return HttpResponseRedirect(reverse('homepages:remove_cart_item', args=[key]))
    except ValueError:
        return HttpResponseRedirect(reverse('homepages:cart'))
    else:
        if 'cart_items' in request.session and key in request.session['cart_items']:
            # Update quantity and total price
            request.session['quantity'] -= int(request.session['cart_items'][key]['quantity'])
            request.session['cart_items'][key]['quantity'] = abs(int(request.GET['quantity']))
            request.session['quantity'] += abs(int(request.GET['quantity']))
            request.session.modified = True
                
            total = 0
            # Recalculate total price considering discounts
            for values in request.session['cart_items']:
                if request.session['cart_items'][values]['discount_active']:
                    total += int((int(request.session['cart_items'][values]['quantity']) * \
                        (int(request.session['cart_items'][values]['price']) 
                        - int(request.session['cart_items'][values]['price']) * \
                        int(request.session['cart_items'][values]['discount']) / 100))/10)*10
                else:
                    total += int(request.session['cart_items'][values]['quantity']) * \
                        int(request.session['cart_items'][values]['price'])

            return render(request, 'cart.html', {'cart_items': request.session['cart_items'], 'total': total})
        
        return HttpResponseRedirect(reverse('homepages:cart'))

@login_required
def remove_all_cart_items(request):
    """Logs out the user by deleting all sessions"""
    del request.session['cart_items']
    del request.session['quantity']
    request.session.modified = True
    return HttpResponseRedirect(reverse('homepages:cart'))