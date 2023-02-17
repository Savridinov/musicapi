from rest_framework.viewsets import ModelViewSet
from .models import Music, Artist, Album, AlbumItem
from .serializers import MusicSerializer, ArtistSerializer, AlbumSerializer, AlbumItemSerializer


class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumItemViewSet(ModelViewSet):
    queryset = AlbumItem.objects.all()
    serializer_class = AlbumItemSerializer
