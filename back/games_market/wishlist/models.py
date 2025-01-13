from django.db import models
from catalog.models import Catalog
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class WishList(models.Model):
    game_information = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist'
