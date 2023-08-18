from django.shortcuts import render, redirect, get_object_or_404
from .models import Barber
from .forms import BarberForm
def list_barbers(request):
    # Fetch all barbers from the database
    barbers = Barber.objects.all()
    return render(request, 'barbers/list.html', {'barbers': barbers})

def add_barber(request):
    if request.method == 'POST':
        form = BarberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_barbers')
    else:
        form = BarberForm()
    return render(request, 'barbers/add.html', {'form': form})

def edit_barber(request, barber_id):
    barber = get_object_or_404(Barber, id=barber_id)
    if request.method == 'POST':
        form = BarberForm(request.POST, request.FILES, instance=barber)
        if form.is_valid():
            form.save()
            return redirect('list_barbers')
    else:
        form = BarberForm(instance=barber)
    return render(request, 'barbers/edit.html', {'form': form})

def delete_barber(request, barber_id):
    barber = get_object_or_404(Barber, id=barber_id)
    if request.method == 'POST':
        barber.delete()
        return redirect('list_barbers')
    return render(request, 'barbers/delete.html', {'barber': barber})
