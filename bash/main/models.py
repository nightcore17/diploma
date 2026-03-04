from django.db import models

class Apparatus(models.Model):
    position = models.CharField("Позиция", max_length=20) # Х-1, К-2
    name = models.CharField("Наименование", max_length=100)
    pressure = models.FloatField("Давление, кгс/см²", default=0.0)
    temperature = models.FloatField("Температура, °C", default=0.0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.position} - {self.name}"