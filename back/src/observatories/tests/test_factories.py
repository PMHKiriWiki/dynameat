from django.test import TestCase
from ..factories import ObservatoryFactory, LocationFactory


class ObservatoryFactoryTests(TestCase):

    def test_observatory_factory_creates_instance(self):
        observatory = ObservatoryFactory.create()
        self.assertIsNotNone(observatory)
        self.assertEqual(type(observatory).__name__, 'Observatory')


    def test_location_factory_creates_instance(self):
        location = LocationFactory.create()
        self.assertIsNotNone(location)
        self.assertEqual(type(location).__name__, 'Location')

