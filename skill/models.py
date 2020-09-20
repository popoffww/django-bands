from django.db import models
from person.models import Person
from membership.models import Membership

class Skill(models.TextChoices):
    play = models.ForeignKey(Membership, on_delete=models.CASCADE)
    LEADGUITAR = 'LG'
    RYTHMGUITAR = 'RG'
    BASSGUITAR = 'BS'
    FLUTE = 'FL'
    ORGAN = 'OR'
    INSTRUMENTS = [
        (LEADGUITAR, 'Lead Guitar'),
        (RYTHMGUITAR, 'Rythm Guitar'),
        (BASSGUITAR, 'Bass Guitar'),
        (FLUTE, 'Flute'),
        (ORGAN, 'Organ'),
    ]

    instruments = models.CharField(max_length=2, choices=INSTRUMENTS,default=LEADGUITAR)
