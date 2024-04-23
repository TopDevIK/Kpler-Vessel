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
        print(data.get('position_time'))
        print(data['position_time'])
        
        if data.get('position_time') and data['position_time'] > timezone.now():
            raise serializers.ValidationError("Position time cannot be in the future.")

    def validate_latitude(self, value):
        if not (self.VALID_NEGATIVE_LATITUDE <= value <= self.VALID_LATITUDE):
            raise serializers.ValidationError("Invalid  latitude")
        return value

    def validate_longitude(self, value):
        if not (-180 <= value <= 180):
            raise serializers.ValidationError("Invalid longitude.")
        return value
