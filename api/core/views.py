
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import VesselPosition
from .serializers import VesselPositionSerializer

class VesselPositionViewSet(viewsets.ModelViewSet):
    queryset = VesselPosition.objects.all()
    serializer_class = VesselPositionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
