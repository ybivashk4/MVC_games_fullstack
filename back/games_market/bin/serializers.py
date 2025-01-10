from rest_framework import serializers
from .models import Bin
from catalog.serializers import CatalogSerializer
from catalog.models import Catalog


class BinSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    game_name_b = CatalogSerializer(read_only=True)
    game_name_b_id = serializers.PrimaryKeyRelatedField(queryset=[Catalog.game_name, ], source=game_name_b,
                                                        write_only=True)
    game_img_b = CatalogSerializer(read_only=True)
    game_img_b_id = serializers.PrimaryKeyRelatedField(queryset=[Catalog.game_img, ], source=game_img_b, write_only=True)

    class Meta:
        model = Bin
        fields = "__all__"
