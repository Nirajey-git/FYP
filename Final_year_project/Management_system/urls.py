from django.urls import path
from . import views
app_name = "Management_system"
urlpatterns = [
 path('patientdashboard/', views.Patient_dashboard, name='patientdashboard'),
 path('doctor-list/', views.doctor_list, name='doctor-list'),
 path('doctor-profile/', views.doctor_profile, name='doctor-profile'),
 path('appointment/', views.appointment, name='appointment'),
 path('appointment-form/', views.appointment_form, name='appointment-form'),
 path('patient-settings/', views.patient_settings, name='patient-settings'),
]