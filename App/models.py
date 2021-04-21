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
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sound"

