from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import  Pet, VeterinaryService

def homepage(request):
    return HttpResponse('<strong>Kućni ljubimci i veterinarske usluge</strong>')

class PetListView(ListView):
    model = Pet
    template_name = './pet_list.html'  
    context_object_name = 'objects'    
    paginate_by = 10                   

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_param = self.request.GET.get('filter', None)
        if filter_param:
            queryset = queryset.filter(your_field__icontains=filter_param)  # Filtriraj prema potrebi
        return queryset


class VeterinaryServiceListView(ListView):
    model = VeterinaryService
    template_name = './veterinaryservice_list.html'  
    context_object_name = 'objects'    
    paginate_by = 10                   

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_param = self.request.GET.get('filter', None)
        if filter_param:
            queryset = queryset.filter(your_field__icontains=filter_param) 
        return queryset


class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    context_object_name = 'object'           


class VeterinaryServiceDetailView(DetailView):
    model = VeterinaryService
    template_name = 'veterinaryservice_detail.html'
    context_object_name = 'object'          