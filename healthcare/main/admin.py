from django.contrib import admin
from .models import UserQuery,Appointment,AppointmentGrant,ScannedBarcode

admin.site.register(UserQuery)
admin.site.register(Appointment)
admin.site.register(AppointmentGrant)
admin.site.register(ScannedBarcode)