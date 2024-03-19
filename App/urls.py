from django.contrib import admin;
from django.urls import path;
from rest_framework import routers;
from django.conf.urls import include;
from .views import SoundViewSet, LocationViewSet, CategoryViewSet, RatingViewSet, ArtistInfoViewSet;
from . import views

router = routers.DefaultRouter()
router.register('sound', SoundViewSet)
router.register('location', LocationViewSet)
router.register('category', CategoryViewSet)
router.register('ratings', RatingViewSet)
router.register('artists', ArtistInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('post_rating/', views.post_rating, name='post_rating'),
] 
