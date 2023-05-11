from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


# СОЗДАНИЕ ДАТЧИКА
class SensorAPICreate(generics.CreateAPIView):
    serializer_class = SensorSerializer


# ИЗМЕНЕНИЕ ДАТЧИКА
class SensorAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# СОЗДАНИЕ ИЗМЕРЕНИЯ
class MeasurementsAPICreate(generics.CreateAPIView):
    serializer_class = MeasurementSerializer

