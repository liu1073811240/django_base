"""
WSGI config for bookmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

# **wsgi.py**是项目与WSGI兼容的Web服务器入口。
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmanager.settings')

application = get_wsgi_application()
