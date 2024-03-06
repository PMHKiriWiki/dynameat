from django.test import TestCase
from ..factories import DeviceFactory


class DeviceFactoryTests(TestCase):

    def test_asteroid_factory_creates_instance(self):
        device = DeviceFactory.create()
        self.assertIsNotNone(device)
        self.assertEqual(type(device).__name__, 'Device')

