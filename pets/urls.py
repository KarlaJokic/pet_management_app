from django.urls import path
from . import views
from .views import PetListView, VeterinaryServiceListView, PetDetailView, VeterinaryServiceDetailView

app_name = 'pets' 

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pets/', PetListView.as_view()),
    path('service/', VeterinaryServiceListView.as_view()),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
]