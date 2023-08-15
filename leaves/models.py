from django.db import models
from barbers.models import Barber

# Leave model representing days off and sick leaves for barbers
class Leave(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)  # Barber the leave is for
    start_date = models.DateField()  # Start date of the leave
    end_date = models.DateField()  # End date of the leave
    LEAVE_TYPES = [
        ('DO', 'Day Off'),
        ('SL', 'Sick Leave'),
        ('V', 'Vacation'),
    ]
    leave_type = models.CharField(max_length=2, choices=LEAVE_TYPES)  # Type of leave

    def __str__(self):
        return f"{self.barber.name} on {self.leave_type} from {self.start_date} to {self.end_date}"
