from django.contrib import admin

from sightings.models import Sighting

class SightingAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_name', 'observatory_name', 'asteroid_name',)
    list_filter = ('device__name', 'observatory__name', 'asteroid__name',)
    ordering = ('-datetime',)

    def device_name(self, obj):
        return obj.device.name
    
    def observatory_name(self, obj):
        return obj.observatory.name
    
    def asteroid_name(self, obj):
        return obj.asteroid.name

admin.site.register(Sighting, SightingAdmin)
