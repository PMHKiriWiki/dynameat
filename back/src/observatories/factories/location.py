import factory

from models import Location

class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    address = factory.fuzzy.FuzzyText(length=16)
    country = factory.fuzzy.FuzzyText(length=16)
    city = factory.fuzzy.FuzzyText(length=16)
    phone = factory.fuzzy.FuzzyInteger()
