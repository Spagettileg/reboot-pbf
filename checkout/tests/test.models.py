from django.test import TestCase
from .models import Order


class CheckoutEntryTest(TestCase):

    def test_string_sample(self):
        order = Order(full_name="bob", phone_number="321",
                      street_address1="house", postcode="345")
        self.assertEqual(str(order.full_name), order.full_name)