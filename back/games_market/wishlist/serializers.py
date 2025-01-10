from rest_framework import serializers
from .models import WishList
from catalog.serializers import CatalogSerializer
from catalog.models import Catalog


class WishListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    rating_w = CatalogSerializer(read_only=True)
    rating_w_id = serializers.PrimaryKeyRelatedField(queryset=[Catalog.rating, ], source=rating_w, write_only=True)

    game_name_w = CatalogSerializer(read_only=True)
    game_name_w_id = serializers.PrimaryKeyRelatedField(queryset=[Catalog.game_name, ], source=game_name_w,
                                                        write_only=True)
    game_img_w = CatalogSerializer(read_only=True)
    game_img_w_id = serializers.PrimaryKeyRelatedField(queryset=[Catalog.game_img, ], source=game_img_w, write_only=True)

    class Meta:
        model = WishList
        fields = "__all__"
