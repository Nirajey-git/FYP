from django.contrib import admin
from .models import Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_Name','last_Name','email','mobile','status')