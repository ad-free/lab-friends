# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

import uuid


class SocialNetwork(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=255, blank=True, null=True)
	facebook = models.CharField(max_length=255, blank=True, null=True)
	twitter = models.CharField(max_length=255, blank=True, null=True)
	github = models.CharField(max_length=255, blank=True, null=True)
	instagrams = models.CharField(max_length=255, blank=True, null=True)
	skype = models.CharField(max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return '{}'.format(self.name)

	def __unicode__(self):
		return '{}'.format(self.name)
