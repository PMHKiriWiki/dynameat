from django.db import models

from commons.models.managers.active_manager import ActiveManager

class ActivableModel(models.Model):
    active = models.BooleanField(default=True)
    
    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
            abstract=True