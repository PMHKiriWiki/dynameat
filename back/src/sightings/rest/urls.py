from rest_framework import routers
from .views.sighting import SightingView

router = routers.SimpleRouter()
router.register(r'sightings', SightingView, basename='sightings')

urlpatterns = router.urls
