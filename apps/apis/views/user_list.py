# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.models import Users as User

# from apps.apis.utils import APIAccessPermission

from apps.commons.utils import Commons
from apps.commons.status import Status

from functools import partial


class Users(APIView):
	""" API Login """

	authentication_classes = []
	permission_classes = []
	# permission_classes = [partial(APIAccessPermission, API().get_api_name('auth', 'login'))]
	renderer_classes = [JSONRenderer]

	# serializer_class = LoginSerializer

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.token = ''
		self.status = Status()
		self.commons = Commons()
		self.message = _('Get user list successfully.')
		self.error_msg = _('Something wrong. Please try again.')

	def post(self, request):
		username = request.data.get('username')
		first_name = request.data.get('first_name')
		obj_user = User.objects.all()

		if obj_user:
			return Response(status=200, data={"message": "User exists."})

		return Response(status=404, data={"message": "User doesn't exists."})
