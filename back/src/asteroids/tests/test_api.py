from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from ..models.asteroid import Asteroid

class AsteroidViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create some test data
        self.asteroid_data = {'name': 'Test Asteroid', 'description': 'A test asteroid', 'matrix_shape': '101011111', 'r_height': 3, 'r_width': 3}
        self.asteroid = Asteroid.objects.create(**self.asteroid_data)
        self.url = reverse('asteroids-detail', kwargs={'pk': self.asteroid.pk})

    def test_list_asteroids(self):
        response = self.client.get(reverse('asteroids-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_asteroid(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.asteroid_data['name'])

    def test_update_asteroid(self):
        updated_data = {'name': 'Updated Asteroid', 'description': 'An updated asteroid', 'matrix_shape': '110011110', 'r_height': 4, 'r_width': 4}
        response = self.client.put(self.url, data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the object from the database
        self.asteroid.refresh_from_db()

        # Check if the object has been updated
        self.assertEqual(self.asteroid.name, updated_data['name'])
        self.assertEqual(self.asteroid.description, updated_data['description'])
        self.assertEqual(self.asteroid.matrix_shape, updated_data['matrix_shape'])
        self.assertEqual(self.asteroid.r_height, updated_data['r_height'])
        self.assertEqual(self.asteroid.r_width, updated_data['r_width'])

    def test_delete_asteroid(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Asteroid.objects.filter(pk=self.asteroid.pk).exists())
