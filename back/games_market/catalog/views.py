from django.shortcuts import render

# Create your views here.
from .models import Catalog
from rest_framework.viewsets import ModelViewSet
from .serializers import CatalogSerializer


class CatalogViewSet(ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()

    def get_queryset(self):
        return Catalog.objects.all()
