from django.contrib import admin

# Register your models here.

from django.contrib.gis import admin
from server.models import Patient, Location, PatientHistory

admin.site.register(Location, admin.GeoModelAdmin)
admin.site.register(Patient)
admin.site.register(PatientHistory)