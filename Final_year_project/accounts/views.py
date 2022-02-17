from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm, DoctorRegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = first_name + " " + last_name 
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            return render(request, 'Login.html')

    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'patient-register.html', context)


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = first_name + " " + last_name 
            license = form.cleaned_data['license']
            user = Account.objects.create_doctor(first_name=first_name, last_name=last_name, email=email, username=username, password=password, license=license)
            user.save()
            return render(request, 'Login.html')

    else:
        form = DoctorRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'doctor-register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        license = ""
        # license = request.POST['license']
        user = auth.authenticate(email=email, password=password)
        request.session['email'] = email
        if len(license) == 8:
            request.session['license'] = license
        if user is not None:
            auth.login(request, user)
            if len(license)==8:
                return redirect('doctor:doctor-dashboard')
            return redirect('Management_system:patientdashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'Login.html')

    return render(request, 'Login.html')

def check_form(request):
    if request.session.has_key("license") and request.session.has_key("email"): 
        return redirect('doctor:doctor-dashboard')
    elif request.session.has_key("email"): 
        return redirect('Management_system:patientdashboard')
    else:
        return redirect('accounts:login')

@login_required(login_url= 'login')
def logout(request):
    try:
        if request.session.has_key("license"):
            del request.session['license'] 
        del request.session['email']
    except:
      pass
    return redirect('accounts:login')

def doctor_register(request):
   return render(request, 'doctor-register.html')


def forget_password(request):
    return render(request, 'forget-password.html')

def google(request):
    print(type(request.session))
    return HttpResponse("googlre hu meh")