from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicViewSet, AlbumViewSet, ArtistViewSet, AlbumItemViewSet

router = DefaultRouter()
router.register('music', MusicViewSet)
router.register('album', AlbumViewSet)
router.register('albumitem', AlbumItemViewSet)
router.register('artist', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls))
]
