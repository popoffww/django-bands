from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    name = forms.CharField(label='',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите название'
                               }
                           ))

    class Meta(object):
        model = Group
        fields = ('name',)