from django.test import TestCase
from .views import (index, adults, bootquality, contact, cookie, explained,
                    faqs, juniors, privacy, terms)


class test_home_directory_pages(TestCase):
    """
    Home page tested to return a positive 200 error code.
    """
    def test_home_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'index.html')

    """
    Adults page tested to return a positive 200 error code.
    """
    def test_adults_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'adults.html')

    """
    Boot quality page tested to return a positive 200 error code.
    """
    def test_boot_quality_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'bootquality.html')

    """
    Contact page tested to return a positive 200 error code.
    """
    def test_contact_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'contact.html')

    """
    Cookie page tested to return a positive 200 error code.
    """
    def test_cookie_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'cookie.html')

    """
    Re-Boot explained page tested to return a positive 200 error code.
    """
    def test_explained_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'explained.html')

    """
    FAQ's page tested to return a positive 200 error code.
    """
    def test_faqs_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'faqs.html')

    """
    Juniors page tested to return a positive 200 error code.
    """
    def test_juniors_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'juniors.html')

    """
    User privacy page tested to return a positive 200 error code.
    """
    def test_privacy_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'privacy.html')

    """
    Terms and conditions page tested to return a positive 200 error code.
    """
    def test_terms_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'terms.html')
