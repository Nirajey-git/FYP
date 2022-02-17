# import forms
# class PatientAppointmentForm(forms.ModelForm):      #used to register an appointment by patient
#     doctor = forms.TypedChoiceField(label='')   #doctor is chosed from existing doctors in hospital database
#     doctor.widget.attrs.update({'class' : 'app-form-control'})
#     #doctorId=forms.CharField(widget=forms.Select(choices=c))  
#     calldate = forms.DateField(label='',widget=SelectDateWidget(years=range(2021,2024)))    #date of appointment
#     calldate.widget.attrs.update({'class' : 'app-form-control-date'})
#     calltime = forms.TypedChoiceField(label='') #time of appointment
#     calltime.widget.attrs.update({'class' : 'app-form-control'})
#     description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'Description'}))
#     description.widget.attrs.update({'class' : 'app-form-control'}) 
#     def __init__(self, *args, **kwargs):
#         super(PatientAppointmentForm, self).__init__(*args, **kwargs)
#         self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]#list of doctors to choose from, taken fresh from database
#         self.fields['calltime'].choices = [('9:00 AM','9:00 AM'),('9:15 AM','9:15 AM'),('9:30 AM','9:30 AM'),('9:45 AM','9:45 AM'),('10:00 AM','10:00 AM'),('10:15 AM','10:15 AM'),('10:30 AM','10:30 AM'),('10:45 AM','10:45 AM'),('11:00 AM','11:00 AM'),('11:15 AM','11:15 AM'),('11:30 AM','11:30 AM'),('11:45 AM','11:45 AM'),('12:00 PM','12:00 PM'),('12:P5 PM','12:15 PM'),('12:30 PM','12:30 PM'),('12:45 PM','12:45 PM'),
#                                             ('14:00 PM','14:00 PM'),('14:15 PM','14:15 PM'),('14:30 PM','14:30 PM'),('14:45 PM','14:45 PM'),('15:00 PM','15:00 PM'),('15:15 PM','15:15 PM'),('15:30 PM','15:30 PM'),('15:45 PM','15:45 PM'),('16:00 PM','16:00 PM'),('16:15 PM','16:15 PM'),('16:30 PM','16:30 PM'),('16:45 PM','16:45 PM'),('17:00 PM','17:00 PM')]
#                                             #choices for time slot for appointment
#     class Meta:
#         model=Appointment
#         fields=['description','calldate','calltime']