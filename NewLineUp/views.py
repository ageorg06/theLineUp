from django.shortcuts import render
from django.http import JsonResponse
from barbers.models import Barber
from django.core import serializers


def landing_page(request):
    barbers = Barber.objects.all()
    barber_data_json = serializers.serialize('json', barbers)
    return render(request, 'landing_page.html', {'barber_data_json': barber_data_json})

def get_appointments(request, barber_id, date):
    # Fetch appointments from the database for the given barber and date
    # For demonstration purposes, I'm returning a static list
    events = [
        {
            'title': 'John Doe',
            'start': date + 'T10:30:00',
            'end': date + 'T11:30:00'
        },
        # ... other events
    ]
    return JsonResponse(events, safe=False)
