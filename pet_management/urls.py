"""
URL configuration for pet_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from pets.views import register
from pets.views import manage_users 
from pets.views import restricted_view
from pets.views import admin_view
from pets.views import PetDetailView
from pets.views import PetListView
from pets.views import VeterinaryServiceDetailView
from pets.views import VeterinaryServiceListView
from pets.views import (
    PetCreateView, PetUpdateView, PetDeleteView,
    VeterinaryServiceCreateView, VeterinaryServiceUpdateView, VeterinaryServiceDeleteView
)

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('manage-users/', manage_users, name='manage_users'),
    path('restricted/', restricted_view, name='restricted_view'),
    path('admin_view/', admin_view, name='admin_view'),
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('vet_services/', VeterinaryServiceListView.as_view(), name='vet_service_list'),
    path('vet_services/<int:pk>/', VeterinaryServiceDetailView.as_view(), name='vet_service_detail'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
     # Create
    path('pets/create/', PetCreateView.as_view(), name='pet_create'),
    path('vet_services/create/', VeterinaryServiceCreateView.as_view(), name='vet_service_create'),

    # Update
    path('pets/<int:pk>/update/', PetUpdateView.as_view(), name='pet_update'),
    path('vet_services/<int:pk>/update/', VeterinaryServiceUpdateView.as_view(), name='vet_service_update'),

    # Delete
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),
    path('vet_services/<int:pk>/delete/', VeterinaryServiceDeleteView.as_view(), name='vet_service_delete'),
]
