from django.db import models
from datetime import datetime

from django.utils import timezone


class Sensor(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')

    class Meta:
        ordering = ['-id']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')

    class Meta:
        ordering = ['-created_at']
