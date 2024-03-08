from django.test import TestCase

# Create your tests here.
class indexTest(TestCase):
    """Testing homepage for index.html"""
    
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)