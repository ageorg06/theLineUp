from django.db import models
from barbers.models import Barber
from customers.models import Customer

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()  # Duration of the service, e.g. 30 minutes for a haircut

    def __str__(self):
        return self.name

# Appointment model representing each booking
class Appointment(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)  # Barber the appointment is with
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Customer the appointment is for
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    start_time = models.TimeField()  # Start time of the appointment
    end_time = models.TimeField()  # End time of the appointment
    date = models.DateField()  # Date of the appointment

    def __str__(self):
        return f"{self.customer.name} with {self.barber.name} on {self.date} at {self.start_time}"
