from django.utils import timezone
from rest_framework import serializers
from .models import VesselPosition


class VesselPositionSerializer(serializers.ModelSerializer):
    
    VALID_LATITUDE = 90
    VALID_NEGATIVE_LATITUDE =  -90
    VALID_LONGITUDE = 180
    VALID_NEGATIVE_LONGITUDE = -180

    class Meta:
        model = VesselPosition
        fields = '__all__'

    def validate(self, data):
        position_time = data.get('position_time')
        
        if position_time > timezone.now():
            raise serializers.ValidationError("Position time cannot be in the future.")
        return data
        
    def validate_latitude(self, value):
        if not (self.VALID_NEGATIVE_LATITUDE <= value <= self.VALID_LATITUDE):
            raise serializers.ValidationError("Invalid  Latitude, Latitude must be between -90 and 90 degrees.")
        return value

    def validate_longitude(self, value):
        if not (self.VALID_NEGATIVE_LONGITUDE <= value <= self.VALID_LONGITUDE):
            raise serializers.ValidationError("Invalid longitude, Longitude must be between -180 and 180 degrees.")
        return value
