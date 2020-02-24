# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator

from apps.address.models import City
from apps.auth.models import User
from apps.social_network.models import SocialNetwork


import uuid

RELATIONSHIP_STATUS = (
	(0, _('Single')),
	(1, _('Married')),
)

SEX_OPTIONS = (
	(0, _('Unknown')),
	(1, _('Male')),
	(2, _('Female')),
)


class Anonymous(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=255)
	email = models.EmailField(blank=True, null=True)
	sex = models.SmallIntegerField(choices=SEX_OPTIONS, default=0)
	avatar = models.FileField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/')
	city = models.ForeignKey(City, blank=True, null=True, related_name='%(class)s_city', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name = 'Anonymous'
		verbose_name_plural = 'Anonymous'


class Users(User):
	phone_number = models.CharField(max_length=100)
	avatar = models.FileField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/')
	sex = models.SmallIntegerField(choices=SEX_OPTIONS, default=0)
	relationship_status = models.SmallIntegerField(choices=RELATIONSHIP_STATUS, default=0)
	is_online = models.BooleanField(default=False, verbose_name=_('Online'))
	city = models.ForeignKey(City, blank=True, null=True, related_name='%(class)s_city', on_delete=models.CASCADE)
	social_network = models.ForeignKey(SocialNetwork, blank=True, null=True, related_name='%(class)s_social_network', on_delete=models.CASCADE)
	anonymous = models.ManyToManyField(Anonymous, blank=True, related_name='%(class)s_anonymous')
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return '{}'.format(self.username)
	
	def __unicode__(self):
		return u'{}'.format(self.username)
	
	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'


class Staff(Users):

	def __str__(self):
		return self.username
	
	def __unicode__(self):
		return u'{}'.format(self.username)
	
	class Meta:
		proxy = True
		verbose_name = 'Staff'
		verbose_name_plural = 'Staffs'
