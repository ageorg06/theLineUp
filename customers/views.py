from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers/list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_customers')
    else:
        form = CustomerForm()
    return render(request, 'customers/add.html', {'form': form})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('list_customers')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/edit.html', {'form': form, 'customer': customer})

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('list_customers')
    return render(request, 'customers/delete.html', {'customer': customer})
