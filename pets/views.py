from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView
from .models import Pet
from .models import VeterinaryService
from datetime import datetime

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# View for managing users, restricted to superusers
@login_required
@user_passes_test(lambda user: user.is_superuser)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

# View restricted to logged-in users
@login_required
def restricted_view(request):
    return render(request, 'restricted.html')

# Function to check if the user is an admin (superuser)
def is_admin(user):
    return user.is_superuser

# View restricted to admin (superuser) users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_only.html')

# ListView for displaying all pets
class PetListView(ListView):
    model = Pet
    template_name = 'pet_management_app/pet_list.html'  # Path to the template
    context_object_name = 'pets'
    paginate_by = 10  # Paginate results

    def get_queryset(self):
        queryset = Pet.objects.all()

        # Filter by user if specified in GET request
        user = self.request.GET.get('user')
        if user:
            queryset = queryset.filter(owner__username=user)

        # Filter by creation date if specified in GET request
        created_after = self.request.GET.get('created_after')
        if created_after:
            queryset = queryset.filter(created__gte=created_after)

        return queryset

# DetailView for displaying the details of a specific pet
class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet_management_app/pet_detail.html'  # Path to the template
    context_object_name = 'pet'


# ListView za prikaz svih veterinarskih usluga
class VeterinaryServiceListView(ListView):
    model = VeterinaryService
    template_name = 'vet_service_list.html'  # Predložak koji ćemo kasnije napraviti
    context_object_name = 'vet_services'

    def get_queryset(self):
        # Filtriranje prema vrsti usluge
        queryset = VeterinaryService.objects.all()
        service_query = self.request.GET.get('service', '')
        if service_query:
            queryset = queryset.filter(service_type__icontains=service_query)  # Pretraživanje prema vrsti usluge
        return queryset

# DetailView za veterinarske usluge
class VeterinaryServiceDetailView(DetailView):
    model = VeterinaryService
    template_name = 'vet_service_detail.html'  # Predložak koji ćemo kasnije napraviti
    context_object_name = 'vet_service'