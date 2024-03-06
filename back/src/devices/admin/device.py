from django.contrib import admin

from devices.models import Device

class DeviceAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'matrix_resolution',)
    list_display = ('id', 'name',)
    search_fields = ('id', 'name')
    ordering = ('-creation_datetime',)

    readonly_fields = ['id']

    # def get_matrix_resolution(self, obj):
    #     return f'{obj.r_height}x{obj.r_width}'

admin.site.register(Device, DeviceAdmin)
