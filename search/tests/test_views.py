from django.test import TestCase, Client
from .views import search
from products.models import Product
from django.contrib import auth
from django.contrib.auth.models import User


class test_search_function(TestCase):
    """
    Test created for the search page to return the correct error status.
    """
    def setUp(self):
        self.user = User.objects.create_user(username="test123",
                                             password="#Qwertyu")
        self.client.login(username="test123", password="#Qwertyu")

    def test_render_search_page(self):
        self.user = User.objects.get(username="test123")
        self.product = Product(make="test")
        self.product.save()
        url = self.client.get('/search/=test')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'products.html')
