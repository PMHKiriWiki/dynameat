import factory

from ..models.device import Device

class DeviceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Device

    name = factory.Faker('text', max_nb_chars=16)
    description = factory.Faker('text', max_nb_chars=256)
    r_height = factory.Faker('random_int', min=0, max=9)
    r_width = factory.Faker('random_int', min=0, max=9)