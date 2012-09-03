import os
import sys

from django.core.handlers.wsgi import WSGIHandler

sys.path.append('/home/guiruduit/webapps/siaconcurseiros_django/siaconcurseiros_django/siaconcurseiros_django')
sys.path.append('/home/guiruduit/webapps/siaconcurseiros_django/siaconcurseiros_django')

os.environ['DJANGO_SETTINGS_MODULE'] = 'siaconcurseiros_django.settings'
application = WSGIHandler()
