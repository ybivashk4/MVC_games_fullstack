from rest_framework import serializers
from descriptions.models import Description


class DescriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Description
        fields = "__all__"
"""
game_base_desc = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    is_multiplayer = models.BooleanField(default=False)
    genre = models.TextField(default="NO genre")
    language = models.TextField(default="English")
    date = models.DateField()
    developer = models.TextField(default="me")
    specialties = models.TextField(default="no specialties")
    description = models.TextField(default="cool game")
    price = models.IntegerField(default="0")
"""