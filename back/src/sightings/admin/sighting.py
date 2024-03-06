from django.contrib import admin

from sightings.models import Sighting

class SightingAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'observatory', 'asteroid',)
    list_filter = ('device', 'observatory', 'asteroid',)
    ordering = ('-datetime',)

    def get_device(self, obj):
        return obj.device.name
    
    def get_observatory(self, obj):
        return obj.observatory.name
    
    def get_asteroid(self, obj):
        return obj.asteroid.name

admin.site.register(Sighting, SightingAdmin)
