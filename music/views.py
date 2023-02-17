from rest_framework.viewsets import ModelViewSet
from .models import Music, Artist, Album
from .serializers import MusicSerializer, ArtistSerializer, AlbumSerializer


class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
