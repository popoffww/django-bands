from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import View, CreateView

from .models import Membership
from .forms import MembershipForm

def home(request):
    search_query_member = request.GET.get('search_member', '')
    if search_query_member:
        members = Membership.objects.get(person__icontains=search_query_member)
    else:
        members = Membership.objects.all()
    return render(request, 'membership/home.html', {'objects_list': members})

# class MembershipCreateView(CreateView):
#     model = Membership
#     form_class = MembershipForm
#     template_name = 'membership/add.html'
#     success_url = reverse_lazy('membership:home')

class MembershipCreate(View):
    def get(self, request):
        form = MembershipForm()
        return render(request, 'membership/add.html', {'form': form})

    def post(self, request):
        bound_form = MembershipForm(request.POST)
        if bound_form.is_valid():
            new_membership = bound_form.save()
            return redirect(new_membership)
        return render(request, 'membership/add.html', {'form': bound_form})





