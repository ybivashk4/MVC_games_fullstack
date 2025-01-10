from django.shortcuts import render

# Create your views here.
from .models import Bin
from rest_framework.viewsets import ModelViewSet
from .serializers import BinSerializer


class BinViewSet(ModelViewSet):
    serializer_class = BinSerializer
    queryset = Bin.objects.all()

    def get_queryset(self):
        return Bin.objects.all()
