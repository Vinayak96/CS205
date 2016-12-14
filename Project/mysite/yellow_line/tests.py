from django.test import TestCase
from .models import *
from django.urls import reverse
# Create your tests here.
from .views import *
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
        user = User.objects.create_user('temporary','temporary@gmail.com', 'temp')

    def test_secure_page(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/yellow_line', follow=True)
        user = User.objects.get(username='temporary')
        self.assertEqual(response.context[email],'temporary@gmail.com')

    
        
        
