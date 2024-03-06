from django.contrib import admin

from observatories.models import Observatory

class ObservatoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('id', 'name')
    ordering = ('-creation_datetime',)

    readonly_fields = ['id']

admin.site.register(Observatory, ObservatoryAdmin)
