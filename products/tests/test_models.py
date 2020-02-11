from django.test import TestCase
from .models import Product


class test_product_entry(TestCase):
    
    """Test product make string"""
    def test_string_sample(self):
        product = Product(make="TestProduct")
        self.assertEqual(str(product), product.make)