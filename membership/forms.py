from django import forms
from .models import Membership, Group, Person

class MembershipForm(forms.ModelForm):
    name = forms.CharField(label='Музыкант', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите имя'}))
    group = forms.CharField(label='Группа', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите название группы'}))
    invite_reason = forms.CharField(label='Причина приглашения', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите причину'}))
    date_joined = forms.DateField(label='Дата')

    class Meta(object):
        model = Membership
        model = Group
        model = Person
        fields = ('name', 'group', 'invite_reason', 'date_joined',)

