from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
