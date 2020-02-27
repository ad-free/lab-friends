# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.authtoken.models import Token
# from rest_framework_jwt.settings import api_settings
from rest_framework.views import Response, exception_handler
from apps.commons.status import Status

import logging


def custom_exception_handler(exc, context):
	response = exception_handler(exc, context)
	commons = Commons()

	if response is not None:
		commons.logs(level=3, message=response.data['detail'], name=context['view'])
		response = commons.response(_status=commons.status.HTTP_4001_UNAUTHORIZED, error_msg=response.data['detail'])

	return response


class Commons:
	"""
	Support multiple function include
	- Support language
	- Reformat response
	- Custom log and dump it to file
	- Init token when the new user register or logout
	- Paginator for pages
	"""

	def __init__(self):
		self.logging = logging.getLogger()
		self.status = Status()

	# self.jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	# self.jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
	# self.jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

	def active_language(self, language):
		try:
			translation.activate(language)
			return True
		except Exception as e:
			self.logs(level=3, message=str(e), name=__name__)
		return False

	def response(self, _status=None, data=None, message=None, error_msg=None):
		return Response({
			'status_code': _status if _status else self.status.HTTP_4000_BAD_REQUEST,
			'result': True if _status == self.status.HTTP_2000_OK else False,
			'data': [data] if data else [],
			'message': message if message else '',
			'errors': [error_msg] if error_msg else []
		}, status=200)

	def logs(self, level: int = 99, message: str = '', name: str = ''):
		""" Storage log here """

		msg = '{} [{}]'.format(name, message)
		if level == 0:
			return message
		if level == 1:
			return self.logging.info(msg)
		elif level == 2:
			return self.logging.warning(msg)
		elif level == 3:
			return self.logging.error(msg)
		else:
			return self.logging.critical(msg)

	def init_token(self, obj_user):
		""" Init the new token """

		try:
			# self.jwt_decode_handler(token)
			token = obj_user.auth_token.key
		except Exception as e:
			self.logs(level=1, message='{} {}'.format(obj_user.username, str(e)), name=__name__)
			# payload = self.jwt_payload_handler(obj_user)
			# token = self.jwt_encode_handler(payload)
			token = Token.objects.create(user=obj_user)
			token = token.key
		# cache.set(obj_user.username, token, getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT))
		return token

	@classmethod
	def paginator(cls, obj, page: int = 1, data_on_page: int = 30):
		paginator = Paginator(obj, data_on_page)
		try:
			data_each_page = paginator.page(page)
		except PageNotAnInteger:
			data_each_page = paginator.page(1)
		except EmptyPage:
			data_each_page = paginator.page(paginator.num_pages)
		return data_each_page
