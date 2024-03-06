import factory

from models import Device

class DeviceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Device

    name = factory.fuzzy.FuzzyText(length=16)
    description = factory.fuzzy.FuzzyText(length=256)
    r_height = factory.fuzzy.FuzzyInteger(0,9)
    r_width = factory.fuzzy.FuzzyInteger(0,9)