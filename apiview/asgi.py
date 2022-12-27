
''' AUTHOR : ROHITH ND (COGNIZANCE AMRITA CHENNAI) '''

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiview.settings')

application = get_asgi_application()
