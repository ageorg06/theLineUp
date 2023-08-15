from django.db import models

# Barber model representing each barber in the shop
class Barber(models.Model):
    name = models.CharField(max_length=100)  # Name of the barber
    working_hours_start = models.TimeField()  # Start time of the barber's working hours
    working_hours_end = models.TimeField()  # End time of the barber's working hours
    phone_number = models.CharField(max_length=15)  # Contact number for the barber
    email = models.EmailField()  # Email address for the barber
    profile_picture = models.ImageField(upload_to='barbers/')  # Barber's profile picture
    bio = models.TextField()  # Short biography or description about the barber
    is_active = models.BooleanField(default=True)  # If the barber is currently active or not

    def __str__(self):
        return self.name
