from django.test import TestCase
from .models import *
from django.urls import reverse
# Create your tests here.
from .views import *
from django.contrib import auth
from django.test import Client
import unittest

class EventTest(TestCase):

    def test_category(self):
        """
        If no events exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('yellow_line:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'yellow_line/index.html')
        self.assertQuerysetEqual(response.context['event_list'], [])


class SimpleTest(TestCase):
    
    def setUp(self):
        self.client=Client()

    def test_that_signed_up_user_gets_logged_in_with_authentication(self):
        response = self.client.post(reverse('yellow_line:signup'),{ 'username':'foo', 'password':'bar'})
        self.assertTemplateUsed(response,'yellow_line/signup.html')
        self.assertEqual(response.status_code, 200)
        self.client.login(username='foo', password='bar')
        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated(),True)
        self.assertIn('_auth_user_id', self.client.session)

    
        
        
