from django.core.validators import MinValueValidator
from django.db import models

class PositiveFloatField(models.FloatField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [MinValueValidator(0.0)]
        super().__init__(*args, **kwargs)
