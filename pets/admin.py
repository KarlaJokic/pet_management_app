from django.contrib import admin
from .models import Pet, VeterinaryService

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'owner_name')

@admin.register(VeterinaryService)
class VeterinaryServiceAdmin(admin.ModelAdmin):
    list_display = ('pet', 'service_date', 'service_type', 'cost')
