import logging

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from sightings.rest.serializers.sighting import SightingSerializer

from sightings.models.sighting import Sighting

from ...models.asteroid import Asteroid

from ..serializers.asteroid import AsteroidSerializer


logger = logging.getLogger(__name__)

class AsteroidView(GenericViewSet, ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = AsteroidSerializer
    

    def get_queryset(self):
        return Asteroid.objects.all().order_by('creation_datetime')

    @action(detail=True, methods=['get'])
    def asteroid_sightings(self, request, pk=None):
        asteroid = self.get_object()
        sightings = Sighting.objects.filter(asteroid=asteroid)
        logger.info(sightings)

        serializer = SightingSerializer(sightings, many=True)

        return Response(serializer.data)