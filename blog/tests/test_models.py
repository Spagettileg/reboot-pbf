from django.test import TestCase
from .models import Item


"""
All tests performed map over to functions in models.py file
"""


class TestItemModel(TestCase):
    def test_item_as_a_string(self):
        # Test name given to object is equal to the item as a string
        item = Item(name="Create a Test")
        self.assertEqual("Create a Test", str(item))
