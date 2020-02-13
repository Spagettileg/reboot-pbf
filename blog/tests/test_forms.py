from django.test import TestCase
from .forms import BlogPostForm


class TestBlogPostForm(TestCase):
    """Test user can create a Blog"""
    def test_users_can_create_a_blog(self):
        form = BlogPostForm({'title', 'author', 'content', 'image',
                             'tag', 'published_date'})
        self.assertTrue(form.is_valid())
