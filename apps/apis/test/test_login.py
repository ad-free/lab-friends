from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from apps.apis.views.user_list import Users
from apps.users.models import Users
from django.urls import reverse
from rest_framework import status


class LoginTestCase(APITestCase):

	def setUp(self):
		print("Test Login")
		self.url = reverse('login')

	def test_login(self):
		data = {
			'username': 'admin',
			'password': 'admin'
		}

		Users.objects.create_user(username="testing", email="testing@gmail.com", password="hello001")

		response = self.client.post(self.url, data, format='json')

		print(response.data)

		self.assertEqual(response.status_code, 200)
