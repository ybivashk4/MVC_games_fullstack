from django.db import models
from catalog.models import Catalog
from catalog.serializers import CatalogSerializer


# Create your models here.

class WishList(models.Model):
    rating_w = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    game_name_w = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    game_img_w = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist'
