from django import forms
from .models import Membership, Person, Group

class MembershipForm(forms.ModelForm):
    name = forms.ModelChoiceField(label='Музыкант',
                                  queryset=Person.objects.all(),
                                  widget=forms.Select(attrs={
                                      'class': 'form-control js-example-basic-single',
                                      'placeholder': 'Введите имя'}))
    group = forms.ModelChoiceField(label='Группа',
                                   queryset=Group.objects.all(),
                                   widget=forms.Select(attrs={
                                       'class': 'form-control js-example-basic-single',
                                       'placeholder': 'Введите название группы'}))

    invite_reason = forms.CharField(label='Причина приглашения',
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Введите причину'}))
    
    date_joined = forms.DateField(label='Дата')

    class Meta(object):
        model = Membership
        fields = ('name', 'group', 'invite_reason', 'date_joined',)

