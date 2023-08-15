from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_barbers, name='list_barbers'),
    path('add/', views.add_barber, name='add_barber'),
    path('edit/<int:barber_id>/', views.edit_barber, name='edit_barber'),
    path('delete/<int:barber_id>/', views.delete_barber, name='delete_barber'),
]
