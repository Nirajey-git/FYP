from django.urls import path
from . import views
app_name = "doctor"
urlpatterns = [
 path('doctor-dashboard/', views.doctor_dashboard, name='doctor-dashboard'),
 path('all-patients/', views.all_patients, name='all-patients'),
 path('new-appointment/', views.new_appointment, name='new-appointment'),
 path('create-invoice/', views.create_invoice, name='create-invoice'),
 path('billing-list/', views.billing, name='billing-list'),
 path('doctor-settings/', views.doctor_settings, name='doctor-settings'),
]