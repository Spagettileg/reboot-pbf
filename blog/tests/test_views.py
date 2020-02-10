from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import Client



class test_views(TestCase):
    """
    accounts app views tests schedule for login, logout, register & profile.
    """
    
    def setUp(self):
        user = User.objects.create(username='test123')
        user.set_password('#Qwertyu')
        user.save()
        self.client = Client()


    def test_login_page(self):
        url = self.client.get('/accounts/login/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, "login.html")
        
    
    def test_login_post(self):
        log_in = {'username':'test123', 'password' : '#Qwertyu'}
        response = self.client.post('/accounts/login/', log_in)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/', status_code=302)
        
    
    def test_user_logged_in(self):
        c = Client()
        c.login(username='test123', password='#Qwertyu')
        client_user = auth.get_user(c)
        user = User.objects.get(username='test123')
        self.assertEqual(client_user, user)


    def test_register_page(self):
        url = self.client.get('/accounts/register/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, "register.html")
        
    
    def test_adding_an_account(self):
        sign_up = {'email': 'test@123test.com',
                                    'username': 'test123',
                                    'password1':'#Qwertyu',
                                    'password2':'#Qwertyu'}
        response = self.client.post('/accounts/register/', sign_up)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/', status_code=302)
        
    
    def test_user_profile_page(self):
        url = self.client.get('/accounts/profile/')
        self.assertEqual(url.status_code, 302)
        self.assertRedirects(url, '/accounts/login/?next=/accounts/profile/',
                             status_code=302)
        
        
    def test_logging_out(self):
        url = self.client.get('/accounts/logout/')
        self.assertEqual(url.status_code, 302)
        self.assertRedirects(url, '/accounts/login/?next=/accounts/logout/',
                             status_code=302)