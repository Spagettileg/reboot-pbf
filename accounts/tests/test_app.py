from django.apps import apps
from django.test import TestCase
from accounts.apps import AccountsConfig

# Test to ensure accounts directory exists within Re-Boot app 
class AccountsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(AccountsConfig.name, 'accounts')
        self.assertEqual(apps.get_app_config('accounts').name, 'accounts')