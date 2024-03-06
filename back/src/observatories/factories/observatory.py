import factory

from models import Observatory
from .location import LocationFactory

class ObservatoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Observatory

    name = factory.fuzzy.FuzzyText(length=16)
    location = factory.SubFactory(LocationFactory)