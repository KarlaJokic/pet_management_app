from django.contrib import admin
from .models import Pet, VeterinaryService
from django.contrib.auth.models import Group

# Omogućavanje pretrage po poljima name i species
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'owner_name')
    search_fields = ['name', 'species']  # Dodajte polja za pretragu

@admin.register(VeterinaryService)
class VeterinaryServiceAdmin(admin.ModelAdmin):
    list_display = ('pet', 'service_date', 'service_type', 'cost')
    search_fields = ['name', 'service_type']  # Dodajte polja za pretragu

# Uklanjanje grupe iz admin sučelja
admin.site.unregister(Group)

# Funkcija koja provjerava je li korisnik administrator
def is_admin(user):
    return user.is_superuser
