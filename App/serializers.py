from rest_framework import serializers;
from .models import Sound, Location, Category
from django.contrib.auth.models import User

class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ['id', 'name', 'duration']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']