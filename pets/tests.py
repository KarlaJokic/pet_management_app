from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Pet, VeterinaryService
from datetime import datetime
from rest_framework.test import APITestCase


#testiranje modela
class PetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.pet = Pet.objects.create(
            name="Bobby",
            species="Dog",
            breed="Labrador",
            age=3,
            owner_name="John Doe",
            owner_contact="123456789"
        )

    def test_pet_creation(self):
        """Testiramo je li ljubimac pravilno kreiran"""
        self.assertEqual(self.pet.name, "Bobby")
        self.assertEqual(self.pet.species, "Dog")
        self.assertEqual(self.pet.breed, "Labrador")

class VeterinaryServiceModelTest(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(
            name="Bobby",
            species="Dog",
            breed="Labrador",
            age=3,
            owner_name="John Doe",
            owner_contact="123456789"
        )
        self.service = VeterinaryService.objects.create(
            pet=self.pet,
            service_date=datetime.now(),
            service_type="Vaccination",
            description="Annual vaccine",
            cost=50.00
        )

    def test_service_creation(self):
        """Testiramo je li veterinarska usluga pravilno kreirana"""
        self.assertEqual(self.service.service_type, "Vaccination")
        self.assertEqual(self.service.description, "Annual vaccine")


#testiranje pogleda
class PetListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        Pet.objects.create(name="Max", species="Dog", breed="Bulldog", age=4, owner_name="Alice", owner_contact="12345")

    def test_pet_list_view(self):
        """Testiramo dohvat liste ljubimaca"""
        response = self.client.get(reverse('pet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Max")


#testiranje API endpointova
class PetAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="apiuser", password="testpassword")
        self.pet = Pet.objects.create(name="Buddy", species="Cat", breed="Siamese", age=2, owner_name="Tom", owner_contact="987654321")

    def test_get_all_pets(self):
        """Testira GET /api/pets/"""
        self.client.force_login(self.user)
        response = self.client.get("/api/pets/")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)
