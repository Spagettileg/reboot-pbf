from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Blog
from django.shortcuts import get_object_or_404


class test_blog_views(TestCase):
    """
    blog app views tests schedule to get blog post, post  blog detail and
    create or edit a blog post.
    """
    
    def test_get_posts(self):
        url = self.client.get('/blog/get_posts/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, "blogposts.html")
        
    
    def test_post_detail(self):
        response = self.client.get('/blog/post_detail/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postdetail.html')
    
    
    def test_new_post(self):
        response = self.client.get('/blog/new_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpostform.html')
        
    
    def test_edit_post(self):
        response = self.client.get('/blog/edit_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogpostform.html')
