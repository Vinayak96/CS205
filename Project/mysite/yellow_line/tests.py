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
        
        
