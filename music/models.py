from django.db import models


class Artist(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.full_name}'


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name='artist', on_delete=models.CASCADE)
    year = models.DateField()

    def __str__(self):
        return f'{self.artist.full_name}'


class Music(models.Model):
    artist = models.ManyToManyField(Artist, related_name='musicartist')
    title = models.CharField(max_length=512)
    number = models.SmallIntegerField()

    def __str__(self):
        return f'{self.number}  {self.title}'
