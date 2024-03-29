from django.db import models


class TimeAuditableModel(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    modification_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True