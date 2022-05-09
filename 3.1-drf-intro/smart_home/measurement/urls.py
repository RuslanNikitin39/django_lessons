from django.contrib import admin
from django.urls import path

from measurement.views import SensorView, SensorRetrieveView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
