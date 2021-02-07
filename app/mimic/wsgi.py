import os

from django.core.wsgi import get_wsgi_application

if "DJANGO_SETTINGS_MODULE" not in os.environ:
    error_message = (
        'You have to put settings through "DJANGO_SETTINGS_MODULE" environment '
        'variable'
    )
    raise Exception(error_message)

application = get_wsgi_application()
