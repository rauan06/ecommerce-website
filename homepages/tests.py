from django.test import TestCase
from django.urls import reverse, resolve
from .models import product, product_category, discount
from . import  views
import json

# Create your tests here.
class TestUrls(TestCase):
    """Testing homepages for urls"""
    
    def test_index(self):
        """Testing index"""
        url = reverse('homepages:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_single(self):
        """Testing single"""
        url = reverse('homepages:single', args=[1])
        self.assertEqual(resolve(url).func, views.single)

    def test_collections(self):
        """Testing collections"""
        url = reverse('homepages:collections', args=['some collection'])
        self.assertEqual(resolve(url).func, views.collections)

    def test_cart(self):
        """Testing cart"""
        url = reverse('homepages:cart')
        self.assertEqual(resolve(url).func, views.cart)

    def test_add_cart(self):
        """Testing add_cart"""
        url = reverse('homepages:add_cart', args=[1])
        self.assertEqual(resolve(url).func, views.add_cart)

    def test_logout(self):
        """Testing logout"""
        url = reverse('homepages:logout_view')
        self.assertEqual(resolve(url).func, views.logout_view)

    def test_remove_cart_item(self):
        """Testing remove_cart_item"""
        url = reverse('homepages:remove_cart_item', args=['some key'])
        self.assertEqual(resolve(url).func, views.remove_cart_item)

    def test_update_total(self):
        """Testing update_total"""
        url = reverse('homepages:update_total', args=['some key'])
        self.assertEqual(resolve(url).func, views.update_total)


class TestViews(TestCase):
    """Testing homepages for GET and POST methods"""
    def setUp(self):
        """Our virtual setUp for out tests"""  # This function is useful, as it can test our queries without changing the databsae

        # Homepages sessions
        self.client.session.update({
            'cart_items': {
                '1m': {
                    'id': 1,
                    'name': "One Piece Hat",
                    'image': "homepages/static/images/one_piece_hat.jpg",
                    'price': 8000,                
                    'discount': 25.00,
                    'discount_active': True,
                    'size': "m",
                    'quantity': 10,
                }
            }
        })

        # Homepages urls
        self.single_url = reverse('homepages:single', args=[1])
        self.collections_url = reverse('homepages:collections', args=['Men'])
        self.cart_url = reverse('homepages:cart')
        self.add_cart_url = reverse('homepages:add_cart', args=[1])
        self.add_cart_error_url = reverse('homepages:add_cart', args=[100])
        self.remove_cart_item_url_error = reverse('homepages:remove_cart_item', args=['rauan'])
        self.remove_cart_item_url = reverse('homepages:remove_cart_item', args=['1m'])

        # Homepages models
        product_category.objects.create(
            name = "Men"
        )

        product.objects.create(
            id =  1,
            name = "One Piece Hat",
            desc = "",
            price = 8000,
            image = "homepages/static/images/one_piece_hat.jpg",
        )

        product.objects.get(id=1).categories.add(product_category.objects.get(name="Men"))

        discount.objects.create(
            product_name = product.objects.get(id=1),
            discount_percent = 25.00,
            active = True,
        )

    def test_single_views(self):
        """Testing single's view function"""
        response = self.client.get(self.single_url) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'single.html')
        self.assertContains(response, "/static/images/one_piece_hat.jpg")

    def test_collections_views(self):
        """Testing collections' view function"""
        response = self.client.get(self.collections_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collections.html')
        self.assertContains(response, "6000")
        
    def test_cart_empty_views(self):
        """Testing empty cart's view function"""
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your cart is empty")

    def test_add_cart_blank(self):
        """Testing add_cart when recieved nothing """
        response = self.client.get(self.add_cart_error_url)
        self.assertEqual(response.status_code, 404)

    def test_add_cart_GET(self):
        """Testing add_cart for GET"""
        response = self.client.get(self.add_cart_url, {"sizes": "m", "quantity": "10"})
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "cart.html")

    def test_remove_cart_item_views_with_error(self):
        """Testing remove_cart_item's view function with error"""
        response = self.client.get(self.remove_cart_item_url_error)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your cart is empty")
        
    def test_remove_cart_item_views(self):
        """Testing remove_cart_item's view function"""
        response = self.client.get(self.remove_cart_item_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your cart is empty")

    def test_update_total(self):
        """"Testing udpate_total's view function"""
