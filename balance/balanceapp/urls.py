
from django.urls import path, include
from . import views

app_name = 'balanceapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('beers', views.beers, name='beers'),
    path('test/<int:test_id>', views.test, name='test')
]
