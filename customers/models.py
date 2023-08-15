from django.db import models
from barbers.models import Barber

# Customer model representing each customer of the shop
class Customer(models.Model):
    name = models.CharField(max_length=100)  # Name of the customer
    phone_number = models.CharField(max_length=15)  # Phone number of the customer
    email = models.EmailField()  # Email address of the customer
    notes = models.TextField(blank=True)  # Additional notes or comments about the customer
    preferred_barber = models.ForeignKey(Barber, on_delete=models.SET_NULL, null=True)  # Customer's preferred barber

    def __str__(self):
        return self.name
