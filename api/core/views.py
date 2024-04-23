
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import VesselPosition
from .serializers import VesselPositionSerializer
from .pagination import StandardResultsSetPagination


class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsSetPagination


class VesselPositionViewSet(BaseModelViewSet):
    queryset = VesselPosition.objects.all()
    serializer_class = VesselPositionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
