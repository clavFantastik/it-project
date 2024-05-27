from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

class Product(Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    img = models.TextField(blank=True)
    rating = models.FloatField(default=0)
    year = models.IntegerField(default=0, blank=True)
    type = models.CharField(choices=[('Книга', 'Книга'), ('Фильм', 'Фильм')], max_length=200, blank=True)
    users = models.ManyToManyField(User, related_name='favorite_products', blank=True)

    def __str__(self):
        return self.title

