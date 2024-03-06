
from commons.rest.fast_serializer import FastSerializer, CharField, IntegerField
from ...models.location import Location

class LocationSerializer(FastSerializer):
    class Meta:
        model = Location

    address = CharField()
    country = CharField()
    city = CharField()
    phone = IntegerField()