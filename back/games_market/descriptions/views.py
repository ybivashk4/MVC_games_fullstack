from django.shortcuts import render

# Create your views here.
from .models import Description
from .serializers import DescriptionSerializer
from rest_framework.viewsets import ModelViewSet


class DescriptionViewSet(ModelViewSet):
    serializer_class = DescriptionSerializer
    queryset = Description.objects.all()

    def get_queryset(self):
        return Description.objects.all()
