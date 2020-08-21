"""
WSGI config for p1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'p1.settings')

application = get_wsgi_application()


# This file allows us to work on the localhost:8000 server for
# testing and working outside of a production server.