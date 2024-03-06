from django.contrib import admin

from asteroids.models import Asteroid


class AsteroidAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name')
    ordering = ('-creation_datetime',)

    readonly_fields = ['id']

admin.site.register(Asteroid, AsteroidAdmin)
