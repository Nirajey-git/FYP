from email.policy import default
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
  
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }), min_length=8)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))
    term = forms.BooleanField(required=True)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password')
    def clean_data(self):
        cleaned_data = super(RegistrationForm, self).clean_data()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'Password did not match'
            )
        email = self.cleaned_data.get('email')
        try:
            Account.objects.get(email=email)
            raise forms.ValidationError(
                'Email already exists'
            )
        except Account.DoesNotExist:
            pass
        
    def __init__(self, *args, **kargs):
        super(RegistrationForm, self).__init__(*args, **kargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'example@domain.com'})
        self.fields['term'].widget.attrs.update({'id': 'term_cond'})

class DoctorRegistrationForm(forms.ModelForm):
  
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }), min_length=8)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))
    license_number = forms.CharField(label='license number', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'license number',
    }))
    term = forms.BooleanField(required=True)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password', 'license_number')
    def clean(self):
        cleaned_data = super(DoctorRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'Password did not match'
            )
        email = self.cleaned_data.get('email')
        try:
            Account.objects.get(email=email)
            raise forms.ValidationError(
                'Email already exists'
            )
        except Account.DoesNotExist:
            pass
        
    def __init__(self, *args, **kargs):
        super(DoctorRegistrationForm, self).__init__(*args, **kargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'example@domain.com'})
        self.fields['license_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Np0865743255'})
        self.fields['term'].widget.attrs.update({'id': 'term_cond'})

# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget= forms.PasswordInput)
#     remember_password = forms.BooleanField()
    
#     def __init__(self, *args, **kargs):
#         super(RegistrationForm, self).__init__(*args, **kargs)
#         self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'password'})
#         self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'example@domain.com'})
#         self.fields['remember_password'].widget.attrs.update({'id': 'remember_password'})
