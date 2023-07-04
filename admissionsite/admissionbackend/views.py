from django.shortcuts import render

# Create your views here.

# import student admission model
from .models import StudentAdmission

# import student admission form
from .forms import StudentAdmissionForm

# render student html page
def index(request):
    return render(request, "index.html")


# create student admission view
def studentAdmission(request):
    # create student admission form
    form = StudentAdmissionForm()
    # check if form is submitted
    if request.method == "POST":
        # pass request data to form
        form = StudentAdmissionForm(request.POST)
        # check if form data is valid
        if form.is_valid():
            # save form data to model
            form.save()
            # create message
            message = "Student Admission Form Submitted Successfully!"
            # return render(request, "studentadmission.html", {"form": form, "message": message})
            return render(request, "studentadmission.html", {"form": form, "message": message})
        else:
            # create message
            message = "Invalid Form Data!"
            # return render(request, "studentadmission.html", {"form": form, "message": message})
            return render(request, "studentadmission.html", {"form": form, "message": message})
    else:
        # return render(request, "studentadmission.html", {"form": form})
        return render(request, "studentadmission.html", {"form": form})
    

# create student admission view
def studentAdmissionUpdate(request, id):
    # get student admission data from model
    studentAdmission = StudentAdmission.objects.get(id=id)
    # create student admission form
    form = StudentAdmissionForm(instance=studentAdmission)
    # check if form is submitted
    if request.method == "POST":
        # pass request data to form
        form = StudentAdmissionForm(request.POST, instance=studentAdmission)
        # check if form data is valid
        if form.is_valid():
            # save form data to model
            form.save()
            # create message
            message = "Student Admission Form Updated Successfully!"
            # return render(request, "studentadmission.html", {"form": form, "message": message})
            return render(request, "studentadmission.html", {"form": form, "message": message})
        else:
            # create message
            message = "Invalid Form Data!"
            # return render(request, "studentadmission.html", {"form": form, "message": message})
            return render(request, "studentadmission.html", {"form": form, "message": message})
    else:
        # return render(request, "studentadmission.html", {"form": form})
        return render(request, "studentadmission.html", {"form": form})
    

# create student admission view
def studentAdmissionDelete(request, id):
    # get student admission data from model
    studentAdmission = StudentAdmission.objects.get(id=id)
    # delete student admission data from model
    studentAdmission.delete()
    # create message
    message = "Student Admission Form Deleted Successfully!"
    # return render(request, "studentadmission.html", {"form": form, "message": message})
    return render(request, "studentadmission.html", {"message": message})