from django.shortcuts import render

# Create your views here.
def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')
    
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