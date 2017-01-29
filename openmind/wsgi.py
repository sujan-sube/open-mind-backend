"""
WSGI config for openmind project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import site

# to setup virtual environment
python_home = '/home/ubuntu/open-mind-backend/venv'
site_packages = python_home + '/lib/python3.5/site-packages'

site.addsitedir(site_packages)



import os, sys

# Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

# Add the path to 3rd party django application and to django itself.
sys.path.append('/home/ubuntu')
os.environ['DJANGO_SETTINGS_MODULE'] = 'openmind.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()