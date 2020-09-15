from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from .models import Person
from .forms import PersonForm

def home(request):
    search_query_person = request.GET.get('search_person', '')
    if search_query_person:
        persons = Person.objects.filter(Q(name__icontains=search_query_person))
    else:
        persons = Person.objects.all()
    return render(request, 'person/home.html', {'objects_list': persons})

class PersonCreateView(SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person/add.html'
    success_url = reverse_lazy('person:home')
    success_message = 'Участник успешно создан'

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('person:home')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


