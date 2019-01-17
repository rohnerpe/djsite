#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

'''
"Fehler" in den Beschreibungen:
Projekt starten in beliebigem Verzeichnis, dann
django-admin startprojekt djsite
Prodiziert ein äusseres und inneres djsite-Verzeichnis. Im äusseren mit manage.py,
im inneren mit __init__.py, settings.py, urls.py und wsgi.py.
In settings.py anpassen:
LANGUAGE_CODE = 'de-ch'
TIME_ZONE = 'UTC/Berlin'
'''