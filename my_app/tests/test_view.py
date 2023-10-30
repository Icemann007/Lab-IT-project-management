from django.test import TestCase
from django.urls import reverse

from my_app.models import Cars

CARS = {"model": "Test", "country": "Ukraine", "age": 5}


class MyappTests(TestCase):
    def test_index_status_code(self):
        response = self.client.get(reverse("my_app:index"))
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get(reverse("my_app:index"))
        self.assertContains(response, "nazar")

    def test_count_cars(self):
        Cars.objects.create(**CARS)
        self.assertEqual(Cars.objects.count(), 1)
