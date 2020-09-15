from django.db import models
from person.models import Person
from group.models import Group

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Музыкант')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    date_joined = models.DateField(verbose_name='Дата')
    invite_reason = models.CharField(max_length=64, verbose_name='Причина приглашения')

    def __str__(self):
            return '{} из группы {}'.format(self.person, self.group)

    class Meta:
        verbose_name = 'Текущий состав'
        verbose_name_plural = 'Текущие составы'

# john = Person.objects.create(name='Джон Леннон')
# paul = Person.objects.create(name='Пол Маккартни')
# george = Person.objects.create(name='Джордж Харрисон')
# ringo = Person.objects.create(name='Ринго Старр')

# mick = Person.objects.create(name='Мик Бокс')
# ken = Person.objects.create(name='Кен Хэнсли')
# david = Person.objects.create(name='Дэвид Байрон')
# gary = Person.objects.create(name='Гэри Тэйн')
# lee = Person.objects.create(name='Ли Керслэйк')

# beatles = Group.objects.create(name='The Beatles')
# uh = Group.objects.create(name='Uriah Heep')

# m1 = Membership.objects.create(person=john, group=beatles, date_joined=('1959-9-6'), invite_reason='Основатель группы')
# m2 = Membership.objects.create(person=paul, group=beatles, date_joined=('1960-8-1'), invite_reason='Нужен новый гитарист')
# m3 = Membership.objects.create(person=george, group=beatles, date_joined=('1960-6-15'), invite_reason='Нужен новый басист')
# m4 = Membership.objects.create(person=ringo, group=beatles, date_joined=('1962-8-16'), invite_reason='Нужен новый барабанщик')

# m5 = Membership.objects.create(person=mick, group=uh, date_joined=('1970-5-20'), invite_reason='Основатель группы')
# m6 = Membership.objects.create(person=ken, group=uh, date_joined=('1970-6-27'), invite_reason='Нужен новый клавишник')
# m7 = Membership.objects.create(person=david, group=uh, date_joined=('1970-5-25'), invite_reason='Нужен новый вокалист')
# m8 = Membership.objects.create(person=gary, group=uh, date_joined=('1972-1-15'), invite_reason='Нужен новый басист')
# m9 = Membership.objects.create(person=lee, group=uh, date_joined=('1972-2-18'), invite_reason='Нужен новый барабанщик')



