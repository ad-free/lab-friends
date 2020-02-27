# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login

from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.apis.serializers.login import LoginSerializer
# from apps.apis.utils import APIAccessPermission

from apps.commons.utils import Commons
from apps.commons.status import Status

from functools import partial


class Login(APIView):
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
		self.message = _('You are successfully logged in.')
		self.error_msg = _('Something wrong. Please try again.')

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')

		if username == 'admin' and password == 'admin':
			return Response(status=200, data={"message": "Login successfully."})
		# return self.commons.response(_status=self.status.HTTP_2000_OK, message=self.message)

		# self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		# serializer = self.serializer_class(data=request.data)
		#
		# if serializer.is_valid():
		# 	obj_user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
		#
		# 	if obj_user is not None:
		# 		data = {
		# 			'token': self.commons.init_token(obj_user)
		# 		}
		# 		login(request, obj_user)
		# 		self.commons.logs(level=1, message=str(obj_user) + ' has successfully logged in.', name=__name__)
		# 		return self.commons.response(_status=self.status.HTTP_2000_OK, data=data, message=self.message)
		# 	self.error_msg = _('User does not exists.')
		# else:
		# 	self.error_msg = serializer.errors
		#
		# self.commons.logs(level=2, message=self.error_msg, name=__name__)
		# return self.commons.response(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
		return Response(status=404, data={"message": "Something wrong. Please try again."})
