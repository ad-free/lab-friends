# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=255)

	def create(self, validated_data):
		pass

	def update(self, instance, validated_data):
		pass
