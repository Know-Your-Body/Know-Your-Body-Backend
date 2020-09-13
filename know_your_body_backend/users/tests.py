from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):

    def test_signup(self):
        """
        Ensure we can signup a new user.
        """
        url = reverse('user-signup')
        data = {'username': 'shashank', 'password': 'mynewpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signin(self):
        """
        Ensure we can signin an existing user.
        """
        url = reverse('user-signup')
        data = {'username': 'shashank', 'password': 'mynewpass'}
        _ = self.client.post(url, data, format='json')

        url = reverse('user-signin')
        data = {'username': 'shashank', 'password': 'mynewpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
