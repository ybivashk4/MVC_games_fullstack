import datetime

from django.db import models


# Create your models here.
class Description(models.Model):
    rating = models.FloatField()
    game_name = models.TextField(default='undef game')
    game_img = models.TextField(default='misc/images/default.png')
    is_multiplayer = models.BooleanField(default=False)
    genre = models.TextField(default="NO genre")
    language = models.TextField(default="English")
    date = models.DateField()
    developer = models.TextField(default="me")
    specialties = models.TextField(default="no specialties")
    description = models.TextField(default="cool game")
    price = models.IntegerField(default="0")

    class Meta:
        db_table = 'games'
