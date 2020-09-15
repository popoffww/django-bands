from django.urls import path
from .views import home, MembershipCreate, MembershipUpdateView, MembershipDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('add', MembershipCreate.as_view(), name='add'),
    path('update/<int:pk>/', MembershipUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MembershipDeleteView.as_view(), name='delete'),
]