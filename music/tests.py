from django.test import TestCase, Client
from .models import Music, Album, Artist


class TestMusicApp(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.artist = Artist.objects.create(full_name='Test artist')

        self.music = Music.objects.create(title='Test music')
        self.music.artist.add(self.artist)

        self.album = Album.objects.create(artist=self.artist, music=self.music, year=2012)

    def test_get_music_list(self):
        response = self.client.get('/music/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test music')
        self.assertIsNotNone(data[0]['id'])
        self.assertEqual(data[0]['artist'])

    def test_get_artist_list(self):
        response = self.client.get('/artist/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test music')
        self.assertIsNotNone(data[0]['id'])
