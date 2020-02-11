from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from products.models import Product
from django.shortcuts import get_object_or_404


class test_product_pages(TestCase):

    def setUp(self):
        self.client = Client()

    """
    Check all rugby boot products can be viewed on same page.
    """
    def test_all_products_view(self):
        page = self.client.get('/products/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'products.html')

    """
    Check rugby boot detail can be viewed.
    """    
    def test_product_detail(self):
        self.user = User.objects.get(username="test123")
        product = Product(title="Test title", category="Test category",
                  colour="Test colour")
        product.save()
        response = self.client.get('/products/{}'.format(product.id))
        self.assertEqual(response.status_code, 301)

    """
    Check to see that a new product creation will successfully render.
    """      
    def test_create_a_product(self):
        response = self.client.get('/products/create_product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_product.html')
