from django.test import TestCase
from ..factories import AsteroidFactory


class AsteroidFactoryTests(TestCase):

    def test_asteroid_factory_creates_instance(self):
        asteroid = AsteroidFactory.create()
        self.assertIsNotNone(asteroid)
        self.assertEqual(type(asteroid).__name__, 'Asteroid')

