import os
import sys

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'siaconcurseiros_django.settings'
application = WSGIHandler()
