from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Group
from .forms import GroupForm

@login_required(login_url='/login/')
def home(request):
    # Поиск
    search_query = request.GET.get('search', '')
    if search_query:
        groups = Group.objects.filter(Q(name__icontains=search_query))
    else:
        groups = Group.objects.all()
    return render(request, 'group/home.html', {'objects_list': groups})

class GroupDetailView(DetailView):
    queryset = Group.objects.all()
    context_object_name = 'object'
    template_name = 'group/detail.html'

class GroupCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Group
    form_class = GroupForm
    template_name = 'group/add.html'
    success_url = reverse_lazy('group:home')
    success_message = 'Группа успешно создана'

class GroupUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Group
    form_class = GroupForm
    template_name = 'group/update.html'
    success_url = reverse_lazy('group:home')
    success_message = 'Группа успешно изменена'

class GroupDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Group
    template_name = 'group/delete.html'
    success_url = reverse_lazy('group:home')


