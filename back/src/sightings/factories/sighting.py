import factory
import datetime
from asteroids.factories import AsteroidFactory
from devices.factories import DeviceFactory
from observatories.factories import ObservatoryFactory

from models import Sighting

class SightingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sighting

    name = factory.fuzzy.FuzzyText(length=16)
    device = factory.SubFactory(DeviceFactory)
    asteroid = factory.SubFactory(AsteroidFactory)
    observatory = factory.SubFactory(ObservatoryFactory)
    datetime = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1))
    device_matrix = '000000100100110110000'