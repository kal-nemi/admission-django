

import django.forms as forms
from .models import StudentAdmission

# create student admission form
class StudentAdmissionForm(forms.ModelForm):
    class Meta:
        model = StudentAdmission
        fields = "__all__"
        
    