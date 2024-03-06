from django.db import models
from commons.models.mixins import BaseModel

class Location(BaseModel):
    address = models.TextField(max_length=128)
    country = models.TextField(max_length=128)
    city = models.TextField(max_length=128)
    phone = models.IntegerField()