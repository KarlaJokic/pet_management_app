import factory
from factory.django import DjangoModelFactory

from pets.models import *

class PetFactory(DjangoModelFactory):
    class Meta:
        model = Pet

    name = factory.Faker("name")
    species = factory.Faker("word")
    breed = factory.Faker("word")
    age = factory.Faker("random_number", digits=1)
    owner_name = factory.Faker("name")
    owner_contact = factory.Faker("phone_number")

class VeterinaryServiceFactory(DjangoModelFactory):
    class Meta:
        model = VeterinaryService

    pet =factory.Iterator(Pet.objects.all())
    service_date = factory.Faker("date_time_this_year")
    service_type = factory.Faker("sentence", nb_words=5)
    description = factory.Faker("paragraph", nb_sentences=3)
    cost=factory.Faker("random_number", digits=3)