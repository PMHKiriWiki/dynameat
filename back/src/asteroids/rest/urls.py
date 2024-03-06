from rest_framework import routers
from ..rest.views.asteroid import AsteroidView

router = routers.SimpleRouter()
router.register(r'asteroids', AsteroidView, basename='asteroids')

urlpatterns = router.urls
