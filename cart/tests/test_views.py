from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import Client
from products.models import Product

class Test_Cart_Views(TestCase):
    """Series of tests to support cart directory views"""
    
    def setUp(self):
        """Logs in a user for our tests"""
        user = User.objects.create_user(username="test123", password="#Qwertyu")
        self.client.login(username="test123", password="#Qwertyu")


    def test_status_codes(self):
        """Test for app to return error status code 200"""
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')

    
    def test_add_to_cart(self):
        """Test for items to be added to cart"""
        user = User(username="test123")
        user.save()

        product = Product(title="test", description="testing", creator=user)
        product.save()
        
        page = self.client.get('/cart/add/{0}'.format(product.id))
        self.assertEqual(page.status_code, 301)