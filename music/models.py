from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


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
    year = models.DateField()

    def __str__(self):
        return f'{self.artist.full_name}'


class AlbumItem(BaseModel):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
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
