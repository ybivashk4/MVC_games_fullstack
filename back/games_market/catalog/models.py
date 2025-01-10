from django.db import models
# from descriptions.models import Description


class Catalog(models.Model):
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
    # some_foreign_key = models.ForeignKey(Description, on_delete=models.CASCADE)

    class Meta:
        db_table = 'games'
# Create your models here.
