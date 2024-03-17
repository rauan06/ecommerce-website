from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestAuth(TestCase):
    def setUp(self):
        self.login_url = reverse("users:login")

        User.objects.create(
            username= 'testuser',
            password= 'testpass',
        )

    def test_login(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpass'})
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
