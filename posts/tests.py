from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        """Create a user for testing and a sample post."""
        self.user = User.objects.create_user(username='dina', password='password')
        self.client.login(username='dina', password='password')  # Log in the user for subsequent tests

    def test_can_list_posts(self):
        """Test that a logged-in user can list posts."""
        Post.objects.create(owner=self.user, title='A title')
        response = self.client.get('/posts/')
        
        # Assert the status code and content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Check that there is at least one post

    def test_logged_in_user_can_create_post(self):
        """Test that a logged-in user can create a new post."""
        response = self.client.post('/posts/', {'title': 'A new title'})
        
        # Assert the post count and response status
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'A new title')  # Ensure the title is correct

    def test_user_not_logged_in_cant_create_post(self):
        """Test that an unauthenticated user cannot create a post."""
        self.client.logout()  # Ensure the user is logged out
        
        response = self.client.post('/posts/', {'title': 'A title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

