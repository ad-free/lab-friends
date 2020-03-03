# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from apps.commons.status import Status
from apps.apis.views.user_list import Users
from apps.users.models import Users as UserModel


class UsersTestCase(APITestCase):

	def setUp(self) -> None:
		print("Testing Users")
		self.url = reverse('user-list')
		UserModel.objects.create_user(
			username="testing",
			email="testing@gmail.com",
			password="hello001"
		)

	def test_users(self):

		data = {
			"username": "admin",
			"first_name": "admin01"
		}

		response = self.client.post(self.url, data=data, format='json')

		print(response.content)
