from django.contrib import admin
from .models import Appointment, ServiceType

# Registering the Barber model with the admin site
admin.site.register(Appointment)
admin.site.register(ServiceType)