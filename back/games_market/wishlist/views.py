from django.shortcuts import render

# Create your views here.
from .models import WishList
from rest_framework.viewsets import ModelViewSet
from .serializers import WishListSerializer


class WishListViewSet(ModelViewSet):
    serializer_class = WishListSerializer
    queryset = WishList.objects.all()

    def get_queryset(self):
        return WishList.objects.all()
