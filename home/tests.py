from django.test import TestCase
from django.urls import resolve
from home.views import dashboard
# Create your tests here.
class DashboardView(TestCase):

    def test_dashboard(self):
        view = resolve('dashboard')
        self.assertEqual(view.func.__name__, dashboard.__name__)