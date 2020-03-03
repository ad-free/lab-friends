# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import routers
from apps.apis.views import login, user_list

# router = routers.DefaultRouter()
# router.register('login', login.Login, basename='login')
# router.register('users', user_list.Users, basename='users')

urlpatterns = [
	# path('', include(router.urls)),
	path('', login.Login.as_view(), name="login"),
	path('users', user_list.Users.as_view(), name="user-list"),
]
