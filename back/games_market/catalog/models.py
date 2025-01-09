from django.db import models
from descriptions.models import Description


class Catalog(models.Model):
    rating = models.FloatField()
    game_name = models.TextField(default='undef game')
    game_img = models.TextField(default='misc/images/default.png')

    class Meta:
        db_table = 'shrot_desc_games'
# Create your models here.
