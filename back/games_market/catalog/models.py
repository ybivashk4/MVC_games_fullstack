from django.db import models


class Catalog(models.Model):
    rating = models.FloatField()
    game_name = models.TextField(default='undef game')
    game_img = models.TextField(default='misc/images/default.png')

    class Meta:
        db_table = 'games'
# Create your models here.
