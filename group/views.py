from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

from .models import Group
from .forms import GroupForm

@login_required(login_url='/login/')
def home(request):
    groups = Group.objects.all()
    return render(request, 'group/home.html', {'objects_list': groups})

class GroupDetailView(DetailView):
    queryset = Group.objects.all()
    context_object_name = 'object'
    template_name = 'group/detail.html'

class GroupUpdateView(SuccessMessageMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'group/update.html'
    success_url = reverse_lazy('group:home')
    success_message = 'Группа успешно изменена'

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'group/delete.html'
    success_url = reverse_lazy('group:home')

