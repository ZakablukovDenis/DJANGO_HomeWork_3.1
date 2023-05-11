from django.db import models


class Sensor(models.Model):
    title_sensor = models.CharField(
        max_length=30,
        blank=False
    )
    description = models.CharField(
        max_length=50,
        blank=True
    )

    def __str__(self):
        return self.title_sensor


class Measurement(models.Model):
    id_sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='id_sensor'
    )
    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
    )
    data_measur = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.id_sensor
