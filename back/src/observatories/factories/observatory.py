import factory

from ..models import Observatory
from .location import LocationFactory

class ObservatoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Observatory

    name = factory.Faker('text', max_nb_chars=16)
    location = factory.SubFactory(LocationFactory)