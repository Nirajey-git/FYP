from django.contrib import admin
from .models import Doctor, Appointment
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_Name','last_Name','email','mobile','status')

@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ('name','patient','email','phone_number','appointment_date', 'appointment_time', 'doctor')