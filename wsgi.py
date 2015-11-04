# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:41:03 2015

@author: Nel
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)