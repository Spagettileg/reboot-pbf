from django.apps import apps
from django.test import TestCase
from blog.apps import BlogConfig


# Test to ensure blog directory exists within Re-Boot app
class BlogsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(BlogConfig.name, 'blog')
        self.assertEqual(apps.get_app_config('blog').name, 'blog')
