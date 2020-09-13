from django.shortcuts import render
from .models import Membership

def home(request):
    members = Membership.objects.all()
    return render(request, 'membership/home.html', {'objects_list': members})
