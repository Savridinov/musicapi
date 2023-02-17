from django.test import TestCase, Client
from .models import Music, Album, Artist, AlbumItem


class TestMusicApp(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.artist = Artist.objects.create(full_name='Test artist')

        self.music = Music.objects.create(title='Test music')
        self.music.artist.add(self.artist)

        self.album = Album.objects.create(artist=self.artist, year=2012)

        self.album = AlbumItem.objects.create(album=self.album, music=self.music)

    def test_get_music_list(self):
        response = self.client.get('/music/')
        data = response.data

        self.assertEqual(data[0]['title'], 'Test music')
        self.assertEqual(data[0]['artist'], [self.artist.id])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['id'])

    def test_get_artist_list(self):
        response = self.client.get('/artist/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEqual(data[0]['full_name'], 'Test artist')

    def test_get_album_list(self):
        response = self.client.get('/album/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEqual(data[0]['year'], 2012)

    def test_get_albumitem_list(self):
        response = self.client.get('/albumitem/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['id'])

    def test_albumitem_music_number(self):
        response = self.client.get('/albumitem/')
        data = response.data
        print(data)
        self.assertEqual(data[0]['number'], 1)
