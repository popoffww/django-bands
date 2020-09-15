from django.db import models

class Person(models.Model):
    name = models.TextField(max_length=128, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Участник группы'
        verbose_name_plural = 'Участники группы'

