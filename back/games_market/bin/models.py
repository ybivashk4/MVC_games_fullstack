from django.db import models
from catalog.models import Catalog


# Create your models here.

class Bin(models.Model):
    game_img_b = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    game_name_b = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bin'
