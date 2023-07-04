from django.db import models

# Create your models here.

# create student admission model
class StudentAdmission(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    # email = models.EmailField()
    # phone = models.CharField(max_length=15)
    # fatherName = models.CharField(max_length=50)
    # motherName = models.CharField(max_length=50)
    # # dateOfBirth = models.DateField()
    # gender = models.CharField(max_length=10)
    # address = models.CharField(max_length=100)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=50)
    # pinCode = models.CharField(max_length=10)
    # country = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName
