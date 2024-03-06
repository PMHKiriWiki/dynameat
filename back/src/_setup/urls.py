from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('asteroids.rest.urls')),
    path('api/', include('sightings.rest.urls')),
    re_path("schema/?", SpectacularAPIView.as_view(), name="schema"),
    re_path(
        "docs/?",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
