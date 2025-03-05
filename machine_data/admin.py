from django.contrib import admin
from .models import SensorReading, SensorExceptionData
# Register your models here.

admin.site.register(SensorReading)
admin.site.register(SensorExceptionData)