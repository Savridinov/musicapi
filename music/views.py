from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Music, Artist, Album, AlbumItem
from .serializers import MusicSerializer, ArtistSerializer, AlbumSerializer, AlbumItemSerializer


class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated]


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]


class AlbumItemViewSet(ModelViewSet):
    queryset = AlbumItem.objects.all()
    serializer_class = AlbumItemSerializer
    permission_classes = [IsAuthenticated]
