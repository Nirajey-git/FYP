from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import  messages
from django.contrib.auth import authenticate, login
from .models import Doctor


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

# def appointment_form(request):
#     if check_admin(request.user):
#         if request.method=="POST":  #if form is submitted
#             appointmentForm = AdminAppointmentForm(request.POST)
#             if appointmentForm.is_valid():
#                 docid=appointmentForm.cleaned_data.get('doctor')    #get doctor id
#                 patid=appointmentForm.cleaned_data.get('patient')   #get patient id
#                 doc = Doctor.objects.all().filter(id=docid).first() #get doctor
#                 pat = Patient.objects.all().filter(id=patid).first()#get patient
#                 if check_avail(doc,appointmentForm.cleaned_data.get('calldate'),appointmentForm.cleaned_data.get('calltime')):  #check if appointment is available during that slot
#                     app = Appointment(patient=pat,doctor=doc,
#                                     description=appointmentForm.cleaned_data.get('description'),
#                                     calldate=appointmentForm.cleaned_data.get('calldate'),
#                                     calltime=appointmentForm.cleaned_data.get('calltime'),
#                                     status=True)    #create new appointment
#                     app.save()
#                     return redirect('bookapp_adm.html')
#                 else:   #if slot is not available, display error
#                     appointmentForm.add_error('calltime', 'Slot Unavailable.')
#                     return render(request,'hospital/Admin/bookapp_adm.html',{'appointmentForm': appointmentForm})
#             else:
#                 print(appointmentForm.errors)
#         else:
#             appointmentForm = AdminAppointmentForm()
#         return render(request,'hospital/Admin/bookapp_adm.html',{'appointmentForm': appointmentForm})
#     else:
#         auth.logout(request)
#         return redirect('login_adm.html')