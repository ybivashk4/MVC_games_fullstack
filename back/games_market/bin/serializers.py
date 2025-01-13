from rest_framework import serializers
from .models import Bin
from catalog.serializers import CatalogSerializer
from catalog.models import Catalog


class BinSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    game_information = CatalogSerializer(read_only=True)
    game_information_id = serializers.PrimaryKeyRelatedField(queryset=Catalog.objects.all(), source="game_information",
                                                             write_only=True)

    class Meta:
        model = Bin
        fields = "__all__"
