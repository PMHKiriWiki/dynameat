from asteroids.models.asteroid import Asteroid
from commons.rest.fast_serializer import FastSerializer, UUIDField, FloatField, CharField, IntegerField

class DeviceSerializer(FastSerializer):
    class Meta:
        model = Asteroid

    id = UUIDField(read_only=True)
    name = CharField()
    r_height = IntegerField()
    r_width = IntegerField()