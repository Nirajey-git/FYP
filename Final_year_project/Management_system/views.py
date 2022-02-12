from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import  messages
from django.contrib.auth import authenticate, login
from .models import Doctor

def user_login(request):
    return render(request, 'Login.html')

def user_register(request):
    return render(request, 'patient-register.html')

def doctor_register(request):
    return render(request, 'doctor-register.html')

def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')

def new_patient(request):
    return render(request, 'new-patient.html')

def all_patients(request):
    return render(request, 'all-patients.html')

def new_appointment(request):
    return render(request, 'new-appointment.html')

def create_invoice(request):
    return render(request, 'create-invoice.html')

def billing(request):
    return render(request, 'billing-list.html')

def doctor_settings(request):
    return render(request, 'doctor-settings.html')

def Patient_dashboard(request):
    return render(request, 'patientdashboard.html')

def doctor_list(request):
    doctor = Doctor.objects.all()
    context = {'doctor': doctor}
    return render(request, 'doctor-list.html', context)

def doctor_profile(request, id):
    doctor = Doctor.objects.all()
    doctor_profile = Doctor.objects.filter(doctor_id=id)
    context = {'doctor': doctor, 'doctor_profile': doctor_profile}

    return render(request, 'doctor-profile.html', context)

def appointment(request):
    return render(request, 'appointment.html')

def appointment_form(request):
    return render(request, 'appointment-form.html')

def patient_settings(request):
    return render(request, 'patient-settings.html')
