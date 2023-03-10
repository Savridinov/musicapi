from django.contrib import admin
from .models import Music, Album, Artist, AlbumItem


@admin.register(Music)
class MudicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', )


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('full_name', )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'year', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('year', 'artist')
    ordering = ('year', )


@admin.register(AlbumItem)
class AlbumItemAdmin(admin.ModelAdmin):
    list_display = ('album', 'music', 'number', 'created_at', 'updated_at')
    search_fields = ('artist', 'music')
    readonly_fields = ('created_at', 'updated_at')
