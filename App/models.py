


from django.db import models

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

# Create your models here.
class Sound(models.Model):
    name = models.TextField()
    duration = models.IntegerField()
    
    #Store audio files on amazon S3?
    audio_file = models.FileField(blank=True, null=True)
    #Store images using amazon S3
    sound_image = models.ImageField(upload_to='photos/', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def category_name(self):
        return str(self.category)

    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

    def location_name(self):
        return str(self.location)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sound"


