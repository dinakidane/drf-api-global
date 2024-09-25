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

class PostDetailViewTests(APITestCase):
    def setUp(self):
        """Create users and posts for testing post detail functionalities."""
        self.dina = User.objects.create_user(username='dina', password='pass')
        self.sarah = User.objects.create_user(username='sarah', password='pass')
        
        self.post_by_dina = Post.objects.create(
            owner=self.dina, title='A title', content='Dina\'s content'
        )
        self.post_by_sarah = Post.objects.create(
            owner=self.sarah, title='Another title', content='Sarah\'s content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        """Test that a post can be retrieved using a valid ID."""
        response = self.client.get(f'/posts/{self.post_by_dina.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'A title')

    def test_cant_retrieve_post_using_invalid_id(self):
        """Test that trying to retrieve a post with an invalid ID returns 404."""
        response = self.client.get('/posts/999/')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        """Test that a user can update their own post."""
        self.client.login(username='dina', password='pass')
        
        response = self.client.put(f'/posts/{self.post_by_dina.id}/', {'title': 'A new title'})
        updated_post = Post.objects.get(pk=self.post_by_dina.id)

        self.assertEqual(updated_post.title, 'A new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        """Test that a user cannot update a post owned by another user."""
        self.client.login(username='dina', password='pass')
        
        response = self.client.put(f'/posts/{self.post_by_sarah.id}/', {'title': 'A new title'})
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
