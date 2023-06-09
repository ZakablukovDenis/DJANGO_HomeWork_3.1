from rest_framework import serializers
from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"


class SensorSerializer(serializers.ModelSerializer):
    id_sensor = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = (
            'id',
            'title_sensor',
            'description',
            'id_sensor'
        )
