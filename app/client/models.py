from django.db import models


class ClientModel(models.Model):

    id = models.IntegerField(primary_key=True, blank=True, null=False)
    name = models.CharField("Name", max_length=50)
    email = models.EmailField("Email", max_length=100)
    password = models.CharField("Password", max_length=50)
    noush = models.IntegerField("Noush", default=0)

    def __str__(self):
        return self.name
