from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Favourite

class FavouriteTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='dina', password='password')
        self.client.login(username='dina', password='password')

        self.other_user = User.objects.create_user(username='sarah', password='password')
        self.post = Post.objects.create(owner=self.other_user, title='A Post')

    def test_user_can_like_post(self):
        response = self.client.post('/api/favourites/', {'post': self.post.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Favourite.objects.filter(user=self.user, post=self.post).exists())

    def test_user_cannot_like_own_post(self):
        own_post = Post.objects.create(owner=self.user, title='My Post')
        response = self.client.post('/api/favourites/', {'post': own_post.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_unlike_post(self):
        Favourite.objects.create(user=self.user, post=self.post)
        response = self.client.delete(f'/api/favourites/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Favourite.objects.filter(user=self.user, post=self.post).exists())

