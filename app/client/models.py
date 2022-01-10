from django.db import models
import uuid
from django.urls import reverse


class ClientModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name
