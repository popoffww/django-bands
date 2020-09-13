from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    name = forms.CharField(label='',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите имя'
                               }
                           ))

    class Meta(object):
        model = Person
        fields = ('name',)