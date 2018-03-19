from django.db import models
from datetime import date
from django.conf import settings


# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class School(models.Model):
    name = models.CharField(max_length=60)
    village = models.CharField(max_length=60)
    taluk = models.CharField(max_length=60)
    dist = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    schoolCode = models.IntegerField(default=999999)
    staffCount = models.IntegerField(default=0)
    stdCount = models.IntegerField(default=0)
    schoolUser = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=60)
    registerNum = models.CharField(max_length=60)
    registerBookNum = models.CharField(max_length=10)
    bloodGroup = models.CharField(max_length=3)
    dob = models.DateField(default=date.today)
    fatherName = models.CharField(max_length=60)
    motherName = models.CharField(max_length=60)
    grandFatherName = models.CharField(max_length=60)
    gender_Choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'))
    gender = models.CharField(max_length=1, choices=gender_Choices)
    pd_Choices = (
        ('Y', 'YES'),
        ('N', 'NO'))
    pd = models.CharField(max_length=1, choices=pd_Choices)
    pdtype = models.CharField(max_length=40, blank=True, null=True)
    pdPercentage = models.IntegerField(default=0)
    admissionDate = models.DateTimeField(auto_now=True)
    standard = models.CharField(max_length=10)
    division = models.CharField(max_length=3)
    adharcardNum = models.IntegerField(default=0)
    caste = models.CharField(max_length=30)
    income = models.FloatField(max_length=30)
    medium_choices = (
        ('K', 'Kannada'),
        ('E', 'English'),
        ('H', 'Hindi'),
        ('M', 'Marathi'),
        ('U', 'Urdu')
    )
    medium = models.CharField(max_length=2, choices=medium_choices)
    casteCertificateNum = models.CharField(max_length=30)
    incomeCertificateNum = models.CharField(max_length=30)
    bankAccNum = models.IntegerField(default=0)
    bank = models.CharField(max_length=30)
    ifscCode = models.CharField(max_length=11)
    photo = models.ImageField(upload_to=upload_location,
                              null=True, blank=True, )

    def __str__(self):
        return self.name
