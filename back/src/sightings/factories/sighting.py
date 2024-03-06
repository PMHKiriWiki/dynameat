import factory

from asteroids.factories.asteroid import AsteroidFactory
from devices.factories.device import DeviceFactory
from observatories.factories.observatory import ObservatoryFactory


from ..models import Sighting

class SightingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sighting
        
    device = factory.SubFactory(DeviceFactory)
    asteroid = factory.SubFactory(AsteroidFactory)
    observatory = factory.SubFactory(ObservatoryFactory)
    datetime = factory.Faker('date_time_this_decade', tzinfo=None)
    device_matrix = '000000100100110110000'