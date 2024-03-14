from django.contrib import admin
from .models import Sound, Category, Location, Rating, ArtistInfo

# Register your models here.
admin.site.register(Sound)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Rating)
admin.site.register(ArtistInfo)
