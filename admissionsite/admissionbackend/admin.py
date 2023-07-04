from django.contrib import admin
import django.contrib.admin as admin
from .models import StudentAdmission
from .forms import StudentAdmissionForm

# Register your models here.

@admin.register(StudentAdmission)
class StudentAdmissionAdmin(admin.ModelAdmin):
    model = StudentAdmission
    form = StudentAdmissionForm
    # fields = ["firstName","lastName"]
    list_display = ["firstName","lastName"]
    

