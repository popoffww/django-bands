from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Membership
from .forms import MembershipForm


def home(request):
    members = Membership.objects.all()
    return render(request, 'membership/home.html', {'objects_list': members})

class MembershipCreateView(CreateView):
    model = Membership
    form_class = MembershipForm
    template_name = 'membership/add.html'
    success_url = reverse_lazy('membership:home')





