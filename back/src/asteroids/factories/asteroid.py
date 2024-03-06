import factory
from factory.faker import Faker

from ..models import Asteroid

class AsteroidFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Asteroid

    name = factory.Faker('text', max_nb_chars=16)
    description = factory.Faker('text', max_nb_chars=256)
    matrix_shape = '101011111'
    r_height = 3
    r_width = 3