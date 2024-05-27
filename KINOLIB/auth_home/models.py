from django.db import models
from django.db.models import Model


class Message(Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    product = models.TextField(blank=True)

    def __str__(self):
        return self.title

