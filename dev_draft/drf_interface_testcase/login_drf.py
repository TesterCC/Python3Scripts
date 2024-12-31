#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/6 15:22'

"""
Test DRF interface by python
"""

from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

# Auth and login
# http://www.django-rest-framework.org/api-guide/testing/#authenticating


# Make all requests in the context of a logged in session.
client = APIClient()
client.login(username='test', password='test123')

# Log out
client.logout()

