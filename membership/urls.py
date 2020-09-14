from django.urls import path
from .views import home, MembershipCreateView

urlpatterns = [
    path('', home, name='home'),
    path('add', MembershipCreateView.as_view(), name='add'),
]