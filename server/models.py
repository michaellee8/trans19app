from django.db import models
from django.contrib.gis.db.models import PointField


# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=200)
    hkid = models.CharField(max_length=20)
    birthday = models.DateField()
    confirmed_day = models.DateField()
    case_num = models.IntegerField()


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    district = models.CharField(max_length=40)
    coordinate = PointField()


class PatientHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                related_name="histories")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True,
                                 related_name="histories")
    start = models.DateField()
    end = models.DateField()
    detail = models.CharField(max_length=400)
    category = models.CharField(max_length=40)
