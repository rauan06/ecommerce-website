from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestAuth(TestCase):
    def setUp(self):
        self.url_login = reverse("users:login")

        User.objects.create(
            username= 'testuser',
            password= 'testpass',
        )

        self.client.login(username= 'testuser', password= 'testpass')

    def test_login(self):
        response = self.client.get(reverse("homepages:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'logout')
