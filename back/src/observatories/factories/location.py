import factory

from ..models import Location

class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    address = factory.Faker('text', max_nb_chars=16)
    country = factory.Faker('text', max_nb_chars=16)
    city = factory.Faker('text', max_nb_chars=16)
    phone = factory.Faker('random_int')
