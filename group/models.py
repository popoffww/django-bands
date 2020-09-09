from django.db import models
from person.models import Person

class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    members = models.ManyToManyField(Person, through='membership.Membership')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
