from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestAuth(TestCase):
    """Testing authentication"""

    def setUp(self):
        self.url_register = reverse("users:register")
        self.url_login = reverse("users:login")
        self.url_logout = reverse("users:logout_view")

        User.objects.create_user(
            username='testuser',
            password='testpass',
        )

    # CONTINUE TOMORROW
    # def test_register(self):
    #     response = self.client.post(self.url_register, {'username':'testuser', 'password1':'testpass','password2':'testpass'},
    #                                 follow=True)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "logout")

    def test_login(self):
        # Testing if the successful login credentials redirect to the index page, and shows the 'logout' message
        self.client.login(username= 'testuser', password= 'testpass')
        response = self.client.post(self.url_login, {'username':'<USERNAME>', 'password':'<PASSWORD>'}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'logout')

    def test_logout(self):
        self.client.post(self.url_login, {'username':'<USERNAME>', 'password':'<PASSWORD>'})
        response = self.client.get(self.url_logout, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Login')
    