from rest_framework import serializers
from .models import Music, Album, Artist, AlbumItem


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumItem
        fields = '__all__'
