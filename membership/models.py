from django.db import models
from person.models import Person
from group.models import Group

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
            return '{} из группы {}'.format(self.person, self.group)

    class Meta:
        verbose_name = 'Текущий состав'
        verbose_name_plural = 'Текущий состав'

# john = Person.objects.create(name='Джон Леннон')
# paul = Person.objects.create(name='Пол Маккартни')
# george = Person.objects.create(name='Джордж Харрисон')
# ringo = Person.objects.create(name=' Ринго Старр')

# beatles = Group.objects.create(name='The Beatles')

# m1 = Membership.objects.create(person=john, group=beatles, date_joined=('1959-9-6'), invite_reason='Основатель группы')
# m2 = Membership.objects.create(person=paul, group=beatles, date_joined=('1960-8-1'), invite_reason='Нужен новый гитарист')
# m3 = Membership.objects.create(person=george, group=beatles, date_joined=('1960-6-15'), invite_reason='Нужен новый басист')
# m4 = Membership.objects.create(person=ringo, group=beatles, date_joined=('1962-8-16'), invite_reason='Нужен новый барабанщик')



