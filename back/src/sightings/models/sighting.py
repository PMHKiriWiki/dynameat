from django.db import models
from asteroids.models.asteroid import Asteroid
from commons.models.mixins import UUIDModel, TimeAuditableModel
from devices.models import Device
from observatories.models import Observatory

class Sighting(UUIDModel, TimeAuditableModel):
    datetime = models.DateTimeField()
    observatory = models.ForeignKey(Observatory, on_delete=models.SET_NULL, related_name='observatory_sightings', null=True)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, related_name='device_sightings', null=True)
    asteroid = models.ForeignKey(Asteroid, on_delete=models.CASCADE, related_name='asteroid_sightings')
    device_matrix = models.TextField(max_length=512)