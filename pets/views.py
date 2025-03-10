from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet, VeterinaryService
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pet
from .serializers import PetSerializer

#homepage
def home_view(request):
    return render(request, 'home.html') 

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

# ListView for displaying all pets with filtering and pagination
class PetListView(ListView):
    model = Pet
    template_name = 'pets/pet_list.html' 
    context_object_name = 'pets'
    paginate_by = 10  

    def get_queryset(self):
        queryset = Pet.objects.all().order_by('id')

        # Filter by name (search functionality)
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(name__icontains=query)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets_list = self.get_queryset()
        paginator = Paginator(pets_list, self.paginate_by)
        page = self.request.GET.get('page')
        pets = paginator.get_page(page)

        context['pets'] = pets  
        return context

# DetailView for displaying the details of a specific pet
class PetDetailView(DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'  
    context_object_name = 'pet'


    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     print(self.object.owner_name, self.object.owner_contact)   # Debugging
     context['veterinary_services'] = VeterinaryService.objects.filter(pet=self.object)
     return context

# ListView for displaying all veterinary services with filtering

class VeterinaryServiceListView(ListView):
    model = VeterinaryService
    template_name = 'vet_services/vet_service_list.html'  # Path to the template
    context_object_name = 'vet_services'
    paginate_by = 10  

    def get_queryset(self):
        queryset = VeterinaryService.objects.all().order_by('id')

        # Filter by service type or date
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(service_type__icontains=query)
       
        date_query = self.request.GET.get('date', '')
        if date_query:
            date_obj = parse_date(date_query) 
            if date_obj:
                queryset = queryset.filter(service_date=date_obj)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_list = self.get_queryset()
        paginator = Paginator(service_list, self.paginate_by)
        v_page = self.request.GET.get('page')
        vet_services = paginator.get_page(v_page)

        context['vet_services'] = vet_services  
        return context


# DetailView for veterinary services
class VeterinaryServiceDetailView(DetailView):
    model = VeterinaryService
    template_name = 'vet_services/vet_service_detail.html' 
    context_object_name = 'vet_service'

# CreateView for Pet
class PetCreateView(CreateView):
    model = Pet
    template_name = 'pets/pet_form.html'  
    fields = ['name', 'species', 'breed', 'age', 'owner_name', 'owner_contact']
    success_url = reverse_lazy('pet_list')

# CreateView for VeterinaryService
class VeterinaryServiceCreateView(CreateView):
    model = VeterinaryService
    template_name = 'vet_services/vet_service_form.html'
    fields = ['pet', 'service_date', 'service_type', 'description', 'cost']
    success_url = reverse_lazy('vet_service_list')  

# UpdateView for Pet
class PetUpdateView(UpdateView):
    model = Pet
    template_name = 'pets/pet_form.html'
    fields = ['name', 'species', 'breed', 'age', 'owner_name', 'owner_contact']
    success_url = reverse_lazy('pet_list')  

# UpdateView for VeterinaryService
class VeterinaryServiceUpdateView(UpdateView):
    model = VeterinaryService
    template_name = 'vet_services/vet_service_form.html'
    fields = ['pet', 'service_date', 'service_type', 'description', 'cost']
    success_url = reverse_lazy('vet_service_list') 

# DeleteView for Pet
class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pets/pet_confirm_delete.html'
    success_url = reverse_lazy('pet_list')  

# DeleteView for VeterinaryService
class VeterinaryServiceDeleteView(DeleteView):
    model = VeterinaryService
    template_name = 'vet_services/vet_service_confirm_delete.html'
    success_url = reverse_lazy('vet_service_list')  


class PetViewSet(viewsets.ModelViewSet):
    """
    API endpoint koji omogućava pregled i uređivanje podataka o ljubimcima.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]  # Ograničava pristup prijavljenim korisnicima

