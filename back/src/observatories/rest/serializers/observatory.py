
from commons.rest.fast_serializer import FastSerializer, CharField, UUIDField, NestedSerializerField
from ..serializers import LocationSerializer
from ...models import Observatory

class ObservatorySerializer(FastSerializer):
    class Meta:
        model = Observatory

    id = UUIDField()
    name = CharField()
    location = NestedSerializerField(serializer_class=LocationSerializer)