import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'yak.settings'

#sys.path.extend(['/home/src', '/home/src/yak', '/home/src/yak/people'])
sys.path.append('/home/src/yak')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
 
