from django.shortcuts import render;
from rest_framework import viewsets;
from rest_framework.response import Response;
from .serializers import SoundSerializer, LocationSerializer, CategorySerializer, RatingSerializer;
from .models import Sound, Category, Location, Rating
from django_filters import rest_framework as filters
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def post_rating(request):
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Return 201 Created status
    return Response(serializer.errors, status=400)

class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        location = self.request.query_params.get('location')
        name = self.request.query_params.get('name')

        if not category and not name:
            return Sound.objects.all()
        elif not category:
            return Sound.objects.filter(name__contains=name)
        elif not name:
            return Sound.objects.filter(category=category)
        else:
            return Sound.objects.filter(category=category, name__contains=name)
    

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

