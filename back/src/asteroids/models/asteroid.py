from django.db import models
from commons.models.mixins import BaseModel

class Asteroid(BaseModel):
    matrix_shape = models.TextField(max_length=512)
    r_height = models.IntegerField(null=True, blank=True)
    r_width = models.IntegerField(null=True, blank=True)