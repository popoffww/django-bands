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
        ordering = ['group', 'date_joined']





# mick = Person.objects.create(name='Мик Бокс')
# ken = Person.objects.create(name='Кен Хэнсли')
# david = Person.objects.create(name='Дэвид Байрон')
# gary = Person.objects.create(name='Гэри Тэйн')
# lee = Person.objects.create(name='Ли Керслэйк')

# uh = Group.objects.create(name='Uriah Heep')

# m1 = Membership.objects.create(person=mick, group=uh, date_joined=('1970-5-20'), invite_reason='Основатель группы')
# m2 = Membership.objects.create(person=ken, group=uh, date_joined=('1970-6-27'), invite_reason='Нужен новый клавишник')
# m3 = Membership.objects.create(person=david, group=uh, date_joined=('1970-5-25'), invite_reason='Нужен новый вокалист')
# m4 = Membership.objects.create(person=gary, group=uh, date_joined=('1972-1-15'), invite_reason='Нужен новый басист')
# m5 = Membership.objects.create(person=lee, group=uh, date_joined=('1972-2-18'), invite_reason='Нужен новый барабанщик')



