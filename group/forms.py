from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    group = forms.CharField(label='',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите название'
                               }
                           ))

    class Meta(object):
        model = Group
        fields = ('group',)