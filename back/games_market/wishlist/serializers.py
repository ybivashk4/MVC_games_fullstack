from rest_framework import serializers
from .models import WishList
from catalog.serializers import CatalogSerializer
from catalog.models import Catalog


class WishListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    game_information = CatalogSerializer(read_only=True)
    game_information_id = serializers.PrimaryKeyRelatedField(queryset=Catalog.objects.all(), source="game_information",
                                                             write_only=True)

    class Meta:
        model = WishList
        fields = "__all__"
