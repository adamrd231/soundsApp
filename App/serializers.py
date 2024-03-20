from rest_framework import serializers;
from .models import Sound, Location, Category, Rating, ArtistInfo
from django.contrib.auth.models import User

class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistInfo
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class SoundSerializer(serializers.ModelSerializer):
    artist = ArtistInfoSerializer()
    category = CategorySerializer()

    class Meta:
        model = Sound
        fields = [
            'id',
            'name',
            'description',
            'artist',
            'audio_file',
            'sound_image',
            'duration',
            'category',
            'location',
            'category_name',
            'location_name',
            'average_rating',
            'free_song',
        ]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'sound', 'rating']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location']


