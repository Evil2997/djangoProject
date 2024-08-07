# djangoProject/__init__.py
from __future__ import absolute_import, unicode_literals

# Это гарантирует, что приложение будет импортировано при запуске Django
from .celery import app as celery_app

__all__ = ('celery_app',)
