from django.urls import path
from .views import home, PersonDeleteView, PersonCreateView

urlpatterns = [
    path('', home, name='home'),
    path('add', PersonCreateView.as_view(), name='add'),
    path('delete/<int:pk>/', PersonDeleteView.as_view(), name='delete'),
]
