"""
ASGI config for balance project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'balance.settings')

application = ProtocolTypeRouter({  #Change to manage websockets from https://www.youtube.com/watch?v=sthCUcw5Zog
    'http': get_asgi_application(),
})
