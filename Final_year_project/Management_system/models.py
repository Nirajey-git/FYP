from django.db import models
from django.contrib.auth.models import User


departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

venue = [('Itahari','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Patient(models.Model):
    firts_Name = models.CharField(max_length=200)
    last_Name = models.CharField(max_length=200)
    email = models.EmailField()
    register = models.DateTimeField(auto_now_add=True)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status=models.BooleanField(default=False)


class Doctor(models.Model):
    first_Name = models.CharField(max_length=200)
    last_Name = models.CharField(max_length=200)
    email = models.EmailField()
    register = models.DateTimeField(auto_now_add=True)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    description = models.TextField(blank=True)

    
class Appointment(models.Model):
    progress_state = [("Pending", "Pending"), ("In Progress", "In Progress"),
                      ("Waiting for receiver", "Waiting for receiver"), ("Delivered", "Delivered")]
    
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=50, default='Itahari')
    phone_number = models.IntegerField()
    sex = models.CharField(max_length=200)
    appointment_date = models.DateField(default='2000-01-01')
    appointment_time = models.TimeField(auto_now=False, auto_now_add=False)
    progress = models.CharField(max_length=50, choices=progress_state, default='Pending')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment_doctor')

class History(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_diseases')
    diseae_name = models.CharField(max_length=40)
    medicine = models.CharField(max_length=40)
    last_checkup =  models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_checkup')


