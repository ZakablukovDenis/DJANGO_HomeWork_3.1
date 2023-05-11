from django.urls import path
from .views import *

urlpatterns = [
    path('sensors', SensorAPICreate.as_view()),
    path('sensors/<int:pk>', SensorAPIUpdate.as_view()),
    path('measurements/', MeasurementsAPICreate.as_view())
]
