import logging

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from ...models.asteroid import Asteroid

from ..serializers.asteroid import AsteroidSerializer


logger = logging.getLogger(__name__)

class AsteroidView(GenericViewSet, ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = AsteroidSerializer
    queryset = Asteroid.objects.all()

