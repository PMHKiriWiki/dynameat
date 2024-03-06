

from asteroids.models.asteroid import Asteroid
from commons.rest.fast_serializer import FastSerializer, UUIDField, CharField, IntegerField

class AsteroidSerializer(FastSerializer):
    class Meta:
        model = Asteroid

    id = UUIDField(read_only=True)
    name = CharField()
    description = CharField()
    matrix_shape = CharField()
    r_height = IntegerField()
    r_width = IntegerField()