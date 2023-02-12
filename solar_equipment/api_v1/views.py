from rest_framework import viewsets
from solar_equipment.models import SolarPanel
from solar_equipment.api_v1.serializers import SolarPanelSerializer


# Create your views here.
class SolarPanelViewSet(viewsets.ModelViewSet):
    queryset = SolarPanel.objects.all()
    serializer_class = SolarPanelSerializer
