
from django.urls import path, include
from . import views

app_name = 'balanceapp'
urlpatterns = [
    path('alerts', views.alerts, name='alerts'),
    path('box_data', views.box_data, name='box_data'),
    path('update_beer_data', views.update_beer_data, name='update_beer_data'),
    path('beers_on_balance', views.beers_on_balance, name='beers_on_balance'),
    path('balance/', views.balances, name='balances'),
    path('balance/<int:balance_id>', views.balance, name='balance'),
    path('matrice_led', views.matrice_led, name='matrice_led'),

    path('beers', views.beers, name='beers'),
    path('beers/<int:beer_id>', views.beer_json, name='beer_data'),
    
    path('data_to_script', views.manage_data_to_script, name='manage_data_to_script'),
    
    path('affond', views.affond, name='affond'),
    path('login', views.login_user, name='login'),
    #path('login_test', include('django.contrib.auth.urls')),
    #path('test/<int:test_id>', views.test, name='test')
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