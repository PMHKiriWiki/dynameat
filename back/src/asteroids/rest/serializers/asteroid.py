

from asteroids.models.asteroid import Asteroid
from commons.rest.fast_serializer import FastSerializer, UUIDField, FloatField, CharField

class AsteroidSerializer(FastSerializer):
    class Meta:
        model = Asteroid

    id = UUIDField(read_only=True)
    name = FloatField()
    matrix_shape = CharField()