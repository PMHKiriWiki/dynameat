from commons.rest.fast_serializer import FastSerializer, UUIDField, CharField, NestedSerializerField, DateTimeField

from asteroids.rest.serializers import AsteroidSerializer
from devices.rest.serializers import DeviceSerializer
from observatories.rest.serializers import ObservatorySerializer

from ...models import Sighting

class SightingSerializer(FastSerializer):
    class Meta:
        model = Sighting

    id = UUIDField(read_only=True)
    device = NestedSerializerField(serializer_class=DeviceSerializer)
    asteroid =  NestedSerializerField(serializer_class=AsteroidSerializer)
    observatory = NestedSerializerField(serializer_class=ObservatorySerializer)
    device_matrix = CharField()
    datetime = DateTimeField()