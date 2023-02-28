from django.contrib import admin

from . models import *
#from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Beer)
admin.site.register(Sale)
admin.site.register(Collectif)
admin.site.register(Message)
admin.site.register(Balance)
admin.site.register(Message_to_send)