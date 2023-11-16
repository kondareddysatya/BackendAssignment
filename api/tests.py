from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Post

User = get_user_model()


class UserRegistrationViewTest(TestCase):
    def test_user_registration(self):
        url = reverse('user-registration')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'john_doe',
            'password': 'securepassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'john_doe')


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )

    def test_user_login(self):
        url = reverse('user-login')
        data = {
            'username': 'test_user',
            'password': 'test_password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)


class PostCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client = APIClient()

    def test_post_creation_authenticated(self):
        url = reverse('post-create')
        data = {
            'content': 'This is a test post.',
        }
        print(self.token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().user, self.user)

    def test_post_creation_unauthenticated(self):
        url = reverse('post-create')
        data = {
            'content': 'This is a test post.',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Post.objects.count(), 0)
