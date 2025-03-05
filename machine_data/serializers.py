from .models import SensorReading, SensorExceptionData
from rest_framework import serializers

class SensorReadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = '__all__'

class SensorExceptionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorExceptionData
        fields = '__all__'