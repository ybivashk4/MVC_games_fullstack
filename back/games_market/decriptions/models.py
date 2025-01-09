import datetime

from django.db import models


# Create your models here.
class Description(models.Model):
    game_name = models.ForeignKey("Catalog")
    rating = models.ForeignKey("Catalog")
    game_img = models.ForeignKey("Catalog")
    is_multiplayer = models.BooleanField(default=False)
    genre = models.TextField(default="NO genre")
    language = models.TextField(default="English")
    date = models.DateField(default=datetime.datetime.now())
    developer = models.TextField(default="me")
    specialties = models.TextField(default="no specialties")
    description = models.TextField(default="cool game")
    price = models.IntegerField(default="0")

    class Meta:
        db_table = 'game_descriptions'
