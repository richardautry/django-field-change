from solar_equipment.models import SolarPanel
from rest_framework import serializers
from solar_equipment.utils import on_change, worker_builder, worker_updater


class SolarPanelSerializer(serializers.ModelSerializer):
    @on_change(field_names=["price", "name"], target=worker_builder)
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = SolarPanel
        fields = ["id", "name", "price"]
