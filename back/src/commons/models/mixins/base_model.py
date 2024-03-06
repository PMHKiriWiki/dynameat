from django.db import models

from .time_auditable_model import TimeAuditableModel
from .uuid_model import UUIDModel

class BaseModel(UUIDModel, TimeAuditableModel):
    name = models.TextField(max_length=128)
    description = models.TextField(max_length=512, blank=True, null=True)

    class Meta:
            abstract=True

