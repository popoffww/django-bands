from django.urls import path
from .views import home, GroupDetailView, GroupUpdateView, GroupDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', GroupDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', GroupUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', GroupDeleteView.as_view(), name='delete'),
]
