from django.contrib import admin
from .models import Pet, VeterinaryService
from django.contrib.auth.models import Group


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'owner_name')

@admin.register(VeterinaryService)
class VeterinaryServiceAdmin(admin.ModelAdmin):
    list_display = ('pet', 'service_date', 'service_type', 'cost')

admin.site.unregister(Group)

def is_admin(user):
    return user.is_superuser

