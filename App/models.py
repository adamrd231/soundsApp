
from django.db import models
from django.contrib.auth.models import User

# Category to setup
class Category(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Category"

class Location(models.Model):
    location = models.TextField()

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = "Location"

class ArtistInfo(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "ArtistInfo"

# Create your models here.
class Sound(models.Model):
    name = models.TextField()
    description = models.TextField()
    artist = models.ForeignKey(ArtistInfo, on_delete=models.CASCADE, blank=True, null=True)
    duration = models.IntegerField()
    free_song = models.BooleanField(default=False)
    
    #Store audio files on amazon S3?
    audio_file = models.FileField(blank=False, null=False, default="")
    #Store images using amazon S3
    sound_image = models.ImageField(upload_to='photos/', null=False, blank=False, default="")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def category_name(self):
        return str(self.category)

    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

    def location_name(self):
        return str(self.location)
    
    def average_rating(self) -> float:
        return Rating.objects.filter(Sound=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Sound"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sound = models.ForeignKey(Sound, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.sound.name}: {self.rating}"
