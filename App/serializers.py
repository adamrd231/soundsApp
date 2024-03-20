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

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'title']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'sound', 'rating']


class SoundSerializer(serializers.ModelSerializer):
    artist = ArtistInfoSerializer()
    category = CategorySerializer() 
    location = LocationSerializer()
    rating_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    def get_rating_count(self, obj):
        return obj.rating_count()

    def get_average_rating(self, obj):
        return obj.average_rating()
    
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
            'rating_count',
            'average_rating',
            'free_song',
        ]


