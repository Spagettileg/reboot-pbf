from django.test import TestCase
from .forms import ProductCreationForm

class test_product_creation_form(TestCase):
    """Test for the product creation form required data fields"""
    def test_required_fields(self):
        form = ProductCreationForm({'make':'', 'colour': 'Product colour'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['make'], ['This field is required.'])
        
        form = ProductCreationForm({'make': 'Test make', 'colour': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['colour'], ['This field is required.'])
        
    """Test for validity of product form when creating a product"""    
    def test_users_can_create_a_product(self):
        form = ProductCreationForm({'make': 'Product make',
                                'colour': 'Product colour'})
        self.assertTrue(form.is_valid())
