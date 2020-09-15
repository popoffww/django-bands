from django.urls import path
from .views import home, MembershipCreate

urlpatterns = [
    path('', home, name='home'),
    path('add', MembershipCreate.as_view(), name='add'),
]