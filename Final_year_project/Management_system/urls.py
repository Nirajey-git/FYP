from django.urls import path
from . import views
urlpatterns = [
 path('', views.user_login, name='login'),
 path('register/', views.user_register, name='register'),
 path('doctor-register/', views.doctor_register, name='doctor-register'),
 path('doctor-dashboard/', views.doctor_dashboard, name='doctor-dashboard'),
 path('new-patient/', views.new_patient, name='new-patient'),
 path('all-patients/', views.all_patients, name='all-patients'),
 path('new-appointment/', views.new_appointment, name='new-appointment'),
 path('create-invoice/', views.create_invoice, name='create-invoice'),
 path('billing-list/', views.billing, name='billing-list'),
 path('doctor-settings/', views.doctor_settings, name='doctor-settings'),
 path('patientdashboard/', views.Patient_dashboard, name='patientdashboard'),
 path('doctor-list/', views.doctor_list, name='doctor-list'),
 path('doctor-profile/', views.doctor_profile, name='doctor-profile'),
 path('appointment/', views.appointment, name='appointment'),
 path('appointment-form/', views.appointment_form, name='appointment-form'),
 path('patient-settings/', views.patient_settings, name='patient-settings'),
]