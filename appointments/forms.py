from django import forms
from .models import Appointment, ServiceType

TIME_SLOTS = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(24) for minute in [0, 30]]

SERVICE_CHOICES = [
    ('Basic Haircut', 'Basic Haircut'),
    ('Shave', 'Shave'),
    ('Beard Trim', 'Beard Trim'),
    ('Hair Wash & Styling', 'Hair Wash & Styling'),
    ('Facial Treatment', 'Facial Treatment'),
]

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentForm(forms.ModelForm):
    start_time = forms.ChoiceField(choices=TIME_SLOTS)
    end_time = forms.ChoiceField(choices=TIME_SLOTS)
    service = forms.ModelChoiceField(queryset=ServiceType.objects.all(), required=True)
    date = forms.DateField(widget=DateInput())
    class Meta:
        model = Appointment
        fields = ['barber', 'customer', 'service', 'start_time', 'end_time', 'date']
