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

# Instantané
class Alert(models.Model):
    ALERT_TYPE = (
        (1, 'Matrice defaut'),
        (2, 'Humidity'),
        (3, 'Temperature'),
        (4, 'B2 NOFut'),
        (5, 'B1 NOFut'),
        (6, 'B2 ENDFut'),
        (7, 'B1 ENDFut'),
        (8, 'B2 Unplug'),
        (9, 'B1 Unplug'),
        (10, 'NB B2 Defaut'),
        (11, 'NB B1 Defaut'),
        (12, 'B2 Def'),
        (13, 'B1 Def'),
        (14, 'Communication Defaut')
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(choices=ALERT_TYPE, null=True, blank=True)  # To prevent errors when the alert is null at the makemigrations

# Update chaque 5 minutes
class BoxData(models.Model):
    # Données dans le boitier
    created_at = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()   #°C
    humidity = models.FloatField()

# Représente l'object bière
class Beer(TimestamptedModel):
    name = models.CharField(max_length = 32)    #A beer is identified by its name
    weight_empty = models.FloatField()   # g
    rho = models.FloatField()    # g/cm3
    quantity = models.FloatField() # cl

    def __tuple__(self):
        return self.name, str(self.weight_empty), str(self.rho), str(self.quantity)
    
# Gère les 2 balances
class Balance(models.Model):
    activated = models.BooleanField()
    related_beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    remaining_beer = models.IntegerField(default=0)   # Nombre de bière restantes
    nomComplet = models.CharField(max_length = 64)
    nomSimple = models.CharField(max_length = 64)
    nameBeerOrCollective = models.BooleanField()

class Message_to_send(models.Model):
    message = models.CharField(max_length = 128)
    permanent = models.BooleanField()
    scroll = models.BooleanField()
    frequence = models.FloatField(default=0.0)

#Represents the number of beers consumed between two moments.
"""
Au moment ou la vente est créé, since (created_at) et until (updated_at) sont mis au temps actuel
A la modification (à l'entrée de volume), juste until est modifié

Toutes les 5 min, une sale est crée par bière sur les futs
"""
class Sale(TimestamptedModel):
    volume = models.FloatField(default=0.0) # cl
    related_beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

#TODO Booleen de balance

class Collectif(models.Model):
    name = models.CharField(max_length = 32)

class Message(models.Model):
    message = models.CharField(max_length = 128)