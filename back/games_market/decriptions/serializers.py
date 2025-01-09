from rest_framework import serializers
from decriptions.models import Description


class DescriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Description
        fields = "__all__"
