from django.test import TestCase

# Create your tests here.
class HomeTestCase(TestCase):
    def test_access(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertTemplateUsed(response, 'frontend/index.html')

    def test_text(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertContains(response, 'Nature\'s RPG')
