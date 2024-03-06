from django.db import models
from commons.models.mixins import BaseModel
from .location import Location

class Observatory(BaseModel):
    location = models.OneToOneField(Location, on_delete=models.DO_NOTHING, related_name='+', null=True)

    class Meta:
        verbose_name = 'Observatory'
        verbose_name_plural = 'Observatories'