from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm


def setUp(self):
    """Test to create a user"""
    user = User.objects.create(username='test123')
    user.set_password('#Qwertyu')
    user.save()


class TestAccountsLoginForm(TestCase):
    """
    Ensure login form is operating as expected
    """
    def test_login_form_valid_data(self):
        user = {'username': 'test123', 'password': '#Qwertyu'}
        form = UserLoginForm(data=user)
        self.assertTrue(form.is_valid)

    def test_login_form_invalid_data(self):
        form = UserLoginForm(data={'username': '', 'password': ''})
        self.assertEqual(form.errors,
                         {'username': ['This field is required.'],
                          'password': ['This field is required.']})


class TestAccountsRegistrationForm(TestCase):
    """
    Ensure registration form is operating as expected
    """
    def test_successfull_register(self):
        form = UserRegistrationForm({'username': "test123",
                                     "password1": "#Qwertyu",
                                     "password2": "#Qwertyu",
                                     "email": "test@123test.com"})
        self.assertTrue(form.is_valid())

    def test_register_with_already_created_username(self):
        setUp(self)
        form = UserRegistrationForm({'username': "test123",
                                     "password1": "#Qwertyu",
                                     "password2": "#Qwertyu",
                                     "email": "test@123test.com"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'],
                                    ['That username already exists.'])

    def test_passwords_match(self):
        form = UserRegistrationForm({'username': 'test123',
                                     'password1': '#Qwertyu1',
                                     'password2': '#Qwertyu2'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'password2': ['Passwords must match!']})

    def test_required_fields(self):
        form = UserRegistrationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors,
                         {'username': ['This field is required.'],
                          'password1': ['This field is required.'],
                          'password2': ['This field is required.']})
