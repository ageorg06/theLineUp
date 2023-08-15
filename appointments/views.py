from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm  # You'll need to create this form

def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/list.html', {'appointments': appointments})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/add.html', {'form': form})

def edit_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('list_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit.html', {'form': form})

def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('list_appointments')
    return render(request, 'appointments/delete.html', {'appointment': appointment})
