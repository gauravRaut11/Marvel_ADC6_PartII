from django.contrib.auth.models import User
from django.test import  TestCase
from .views import register, login
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

class Test_User(TestCase):

    def test_user_authentication(self):
        user = authenticate(username='admin', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)

