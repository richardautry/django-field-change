from django.urls import path, include
from rest_framework import routers
from solar_equipment.api_v1.views import SolarPanelViewSet


router = routers.DefaultRouter()
router.register(r'solar_panels', SolarPanelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
