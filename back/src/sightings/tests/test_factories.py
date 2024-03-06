from django.test import TestCase
from ..factories import SightingFactory


class SightingFactoryTests(TestCase):

    def test_asteroid_factory_creates_instance(self):
        sighting = SightingFactory.create()
        self.assertIsNotNone(sighting)
        self.assertEqual(type(sighting).__name__, 'Sighting')

