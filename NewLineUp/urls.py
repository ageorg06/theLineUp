"""
URL configuration for NewLineUp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from NewLineUp.views import landing_page
from NewLineUp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('barbers/', include('barbers.urls')),
    path('customers/', include('customers.urls')),
    path('appointments/', include('appointments.urls')),
    path('leaves/', include('leaves.urls')),
    path('', landing_page, name='landing_page'),
    path('get_appointments/<int:barber_id>/<str:date>/', views.get_appointments, name='get_appointments'),
    path('update_appointment_time/', views.update_appointment_time, name='update_appointment_time'),
]
