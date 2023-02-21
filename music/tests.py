from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Music, Album, Artist, AlbumItem
from rest_framework_jwt.compat import get_user_model


User = get_user_model()

class BaseTestCase(TestCase):
    def setUp(self) -> None:
        self.username = 'tester'
        self.password = 'password'
        self.email = 'test@example.com'

        self.user = User.objects.create_user(self.username, self.email, self.password)

        self.data = {
            'username': self.username,
            'password': self.password
        }

        self.client = APIClient(enforce_csrf_checks=True)

        self.artist = Artist.objects.create(full_name='Test artist')

        self.music = Music.objects.create(title='Test music')
        self.music.artist.add(self.artist)

        self.album = Album.objects.create(artist=self.artist, year=2012)

        self.album = AlbumItem.objects.create(album=self.album, music=self.music)

        response = self.client.post('/api/token/', self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.refresh = response.json()['refresh']
        self.access = response.json()['access']

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.access)

    def test_jwt_login(self):
        self.client = APIClient(enforce_csrf_checks=True)

        response = self.client.post('/api/token/', self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.refresh = response.json()['refresh']
        self.access = response.json()['access']

        resp = self.client.post('/api/token/verify/', {'token': self.access}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post('/api/token/verify/', {'token': 'test'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

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

        self.assertEqual(data[0]['number'], 1)
