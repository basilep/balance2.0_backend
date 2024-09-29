from django.apps import AppConfig
import threading
import os

class BalanceappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'balanceapp'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true':    # Use for singleton
            from .views import start_web_socket_server
            # Start the WebSocket server in a separate thread
            threading.Thread(target=start_web_socket_server, daemon=True).start()
            

