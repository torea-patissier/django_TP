from django.db import models
from django.utils import timezone


class Artiste(models.Model):
    POP = 'POP'
    RAP = 'RAP'
    CLASSIC = 'CLASSIC'
    ROCK = 'ROCK'
    UNDEFINED = 'UNDEFINED'
    STYLE_CHOICES = [
        (POP, 'Pop'),
        (RAP, 'Rap'),
        (CLASSIC, 'Classic'),
        (ROCK, 'Rock'),
        (UNDEFINED, 'Undefined'),
    ]
    nom = models.CharField(max_length=255)
    style = models.CharField(max_length=50, choices=STYLE_CHOICES, default=UNDEFINED)


class Chanson(models.Model):
    titre = models.CharField(max_length=255)
    duree = models.DurationField()
    date = models.DateTimeField(default=timezone.now)
    artiste = models.ForeignKey(Artiste, on_delete=models.PROTECT)
