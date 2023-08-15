from django import forms

from .utils import generate_time_choices
from .models import Barber

class BarberForm(forms.ModelForm):
    working_hours_start = forms.ChoiceField(choices=generate_time_choices(), widget=forms.Select(attrs={'class': 'form-control'}))
    working_hours_end = forms.ChoiceField(choices=generate_time_choices(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Barber
        fields = ['name', 'working_hours_start', 'working_hours_end', 'phone_number', 'email', 'profile_picture', 'bio', 'is_active']
