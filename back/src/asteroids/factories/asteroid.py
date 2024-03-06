import factory

from models import Asteroid

class AsteroidFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Asteroid

    name = factory.fuzzy.FuzzyText(length=16)
    description = factory.fuzzy.FuzzyText(length=256)
    matrix_shape= '10101111'
