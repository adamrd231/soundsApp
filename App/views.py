from django.shortcuts import render;
from rest_framework import viewsets;
from rest_framework.response import Response;

from .serializers import SoundSerializer, LocationSerializer, CategorySerializer;
from .models import Sound, Category, Location

# Create your views here.
class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer