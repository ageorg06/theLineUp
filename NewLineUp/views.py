from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from barbers.models import Barber
from appointments.models import Appointment
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


def landing_page(request):
    barbers = Barber.objects.all()
    barber_data_json = serializers.serialize('json', barbers)
    return render(request, 'landing_page.html', {'barber_data_json': barber_data_json})

def get_appointments(request, barber_id, date):
    appointments = Appointment.objects.filter(barber_id=barber_id, date=date)
    events = []
    for appointment in appointments:
        events.append({
            'title' : appointment.customer.name,
            'start' : str(appointment.date) + 'T' + str(appointment.start_time),
            'end' : str(appointment.date) + 'T' + str(appointment.end_time),
            'appointment_id': appointment.id
        })
    return JsonResponse(events, safe=False)


@csrf_exempt
def update_appointment_time(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        new_start_time = request.POST.get('new_start_time')
        new_end_time = request.POST.get('new_end_time')
        print(new_start_time)
        try:
            # Fetch the appointment from the database
            appointment = Appointment.objects.get(id=appointment_id)
            
            # Convert the new start and end times to Python datetime.time objects
            new_start_time_obj = datetime.strptime(new_start_time, '%Y-%m-%dT%H:%M:%S.%fZ').time()
            new_end_time_obj = datetime.strptime(new_end_time, '%Y-%m-%dT%H:%M:%S.%fZ').time()

            
            # Update the start and end times
            appointment.start_time = new_start_time_obj
            appointment.end_time = new_end_time_obj
            print("Start" ,appointment.start_time)
            print("End" , appointment.end_time)
            appointment.save()

            return JsonResponse({'status': 'success'})

        except Appointment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Appointment not found'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid date/time format'})

    return HttpResponseBadRequest('Invalid request method')

