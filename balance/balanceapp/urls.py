
from django.urls import path, include
from . import views

app_name = 'balanceapp'
urlpatterns = [
    path('beers', views.beers, name='beers'),
    path('beers_data', views.beers_json, name='beers_data'),
    path('message_data', views.message_to_script, name='message_data'),
    path('message', views.message, name='message'),
    path('affond', views.affond, name='affond'),
    path('login', views.login_user, name='login'),
    #path('login_test', include('django.contrib.auth.urls')),
    path('test/<int:test_id>', views.test, name='test')
]


"""
Before remove every pages and keep just data
urlpatterns = [
    path('', views.index, name='index'),
    path('beers', views.beers, name='beers'),
    path('beers_data', views.beers_json, name='beers_data'),
    path('message_data', views.message_to_script, name='message_data'),
    path('message', views.message, name='message'),
    path('affond', views.affond, name='affond'),
    path('login', views.login_user, name='login'),
    #path('login_test', include('django.contrib.auth.urls')),
    path('test/<int:test_id>', views.test, name='test')
]
"""