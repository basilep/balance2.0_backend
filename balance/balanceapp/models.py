from django.contrib.auth.models import User
from django.db import models
from enum import Enum

# TODO constraints

# Create your models here.

class TimestamptedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Beer(TimestamptedModel):
    name = models.CharField(max_length = 32)
    weight_empty = models.FloatField()   # g
    rho = models.FloatField()    # g/cm3
    quantity = models.FloatField() # cl

    def __tuple__(self):
        return self.name, str(self.weight_empty), str(self.rho), str(self.quantity)

#Represents the number of beers consumed between two moments.
"""
Au moment ou la vente est créé, since (created_at) et until (updated_at) sont mis au temps actuel
A la modification (à l'entrée de volume), juste until est modifié

Toutes les 5 min, une sale est crée par bière sur les futs
"""
class Sale(TimestamptedModel):
    volume = models.FloatField(default=0.0) # cl
    related_beer = models.ForeignKey(Beer, on_delete=models.CASCADE)


class BalanceData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()   #°C
    humidity = models.FloatField()

class Collectif(models.Model):
    name = models.CharField(max_length = 32)

class Message(models.Model):
    message = models.CharField(max_length = 128)


class Alert(models.Model):
    ALERT_TYPE = (
        (1, 'OverWeight'),
        (2, 'NoFut'),
        (3, 'EndFut'),
        (4, 'OverHeat'),
        (5, 'OverHumidity'),
        (6, 'NoBalance'),
        (7, 'NoLedScreen'),

    )
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(choices=ALERT_TYPE, null=True, blank=True)  #To change ?
    data = models.TextField(default=None)   #TODO change it to json