from django.contrib import admin;
from django.urls import path;
from rest_framework import routers;
from django.conf.urls import include;
from .views import SoundViewSet, LocationViewSet, CategoryViewSet, RatingViewSet;

router = routers.DefaultRouter()
router.register('sound', SoundViewSet)
router.register('location', LocationViewSet)
router.register('category', CategoryViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
] 
