from django.test import TestCase
from django.urls import reverse


class IndexTest(TestCase):
    def test_get_root(self):
        response = self.client.get(reverse('pika_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pika home")
        self.assertContains(response, "Oh, hi!")
