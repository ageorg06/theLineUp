from django.contrib import admin
from .models import Customer

# Registering the Customer model with the admin site
admin.site.register(Customer)
