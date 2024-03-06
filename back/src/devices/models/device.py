from django.db import models
from commons.models.mixins import BaseModel

class Device(BaseModel):
    r_height = models.IntegerField()
    r_width = models.IntegerField()