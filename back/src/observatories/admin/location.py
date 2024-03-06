from django.contrib import admin

from observatories.models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'country', 'city', 'phone',)
    search_fields = ('id', 'name')
    ordering = ('-creation_datetime',)

    readonly_fields = ['id']


admin.site.register(Location, LocationAdmin)
