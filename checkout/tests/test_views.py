from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User


class test_checkout_views(TestCase):
    """test for login"""
    def setUp(self):
        self.user = User.objects.create_user(username="test123",
                                             password="#Qwertyu")
        self.client.login(username="test123", password="#Qwertyu")

    """test rendering of checkout page via 200 error code generation."""
    def test_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')
