from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=[
        ('pas', 'Pas'),
        ('mačka', 'Mačka'),
        ('ptica', 'Ptica'),
        ('drugo', 'Drugo'),
    ])
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField()
    owner_name = models.CharField(max_length=100)
    owner_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.species})"

class VeterinaryService(models.Model):
    SERVICE_CHOICES = [
        ('cijepljenje', 'Cijepljenje'),
        ('pregled', 'Generalni pregled'),
        ('operacija', 'Operacija'),
        ('dental', 'Dentalni zahvat'),
        ('šišanje', 'Šišanje'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_service_type_display()} for {self.pet.name} on {self.service_date}"
