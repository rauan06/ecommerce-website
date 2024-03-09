from django.test import TestCase
from django.urls import reverse, resolve
from . import  views

# Create your tests here.
class TestUrls(TestCase):
    """Testing homepages for urls"""
    
    def test_index(self):
        """Testing index"""
        url = reverse('homepages:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_single(self):
        """Testing single"""
        url = reverse('homepages:single', args=[3])
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
    pass