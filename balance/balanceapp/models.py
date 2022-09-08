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
    tare = models.FloatField()   # g
    rho = models.FloatField()    # g/cm3

    def __tuple__(self):
        return self.name, str(self.tare), str(self.rho)

#Represents the number of beers consumed between two moments.

"""
Au moment ou la vente est créé, since (created_at) et until (updated_at) sont mis au temps actuel
A la modification (à l'entrée de volume), juste until est modifié

Toutes les 5 min, une sale est crée par bière sur les futs
"""
class Sale(TimestamptedModel):
    volume = models.FloatField(default=0.0) # cl
    related_beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

class AlertType(Enum):
    Overheating = "Overheating"
    ScaleConnectionLost = "ScaleConnectionLost"
    ServerConnectionLost = "ServerConnectionLost"
    DisplayConnectionLost = "DisplayConnectionLost"
    NoBarrel = "NoBarrel"

class Alert(models.Model):
    type = AlertType
    data = models.TextField(default=None)   #TODO change it to json