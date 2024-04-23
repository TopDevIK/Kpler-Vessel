from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VesselPositionViewSet


router = DefaultRouter()
router.register(r'vessels', VesselPositionViewSet, basename='vessels')

urlpatterns = [
    path('', include(router.urls)),
]
