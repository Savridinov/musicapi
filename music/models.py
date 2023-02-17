from django.db import models


#Can't solve the problem music.Album.artist: (models.E006) The field 'artist' clashes with the field 'artist' from model 'music.basemodel'.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Artist(BaseModel):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.full_name}'


class Music(BaseModel):
    artist = models.ManyToManyField(Artist, related_name='musicartist')
    title = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.title}'


class Album(BaseModel):
    artist = models.ForeignKey(Artist, related_name='artist', on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.artist.full_name}'


class AlbumItem(BaseModel):
    album = models.ForeignKey(Album, related_name='albumitem', on_delete=models.CASCADE)
    music = models.ForeignKey(Music, related_name='albumitem', on_delete=models.CASCADE)
    number = models.SmallIntegerField()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        albomitem = AlbumItem.objects.last()
        if albomitem:
            self.number = albomitem.number + 1
        else:
            self.number = 1
        return super(AlbumItem, self).save()

    def __str__(self):
        return f'{self.number}  {self.music}  {self.album}'
