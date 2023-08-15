from django.shortcuts import render
from .models import Leave

def list_leaves(request):
    # Fetch all leaves from the database
    leaves = Leave.objects.all()
    return render(request, 'list.html', {'leaves': leaves})
