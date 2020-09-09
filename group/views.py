from django.shortcuts import render
from .models import Group

def home(request):
    groups = Group.objects.all()
    return render(request, 'group/home.html', {'objects_list': groups})


