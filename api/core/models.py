from django.db import models


class VesselPosition(models.Model):
    vessel_id = models.CharField(max_length=50)
    position_time = models.DateTimeField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    def __str__(self) -> str:
        return self.vessel_id
