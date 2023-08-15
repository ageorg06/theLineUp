from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_appointments, name='list_appointments'),
    path('add/', views.add_appointment, name='add_appointment'),
    path('edit/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
]