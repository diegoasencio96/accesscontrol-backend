from django.db import models
from apps.users.models import Profile

# Create your models here.

class DoorOpening(models.Model):
    date = models.DateField(verbose_name='Fecha de apertura')
    time = models.TimeField(verbose_name='Hora de apertura')
    user = models.ForeignKey(Profile, verbose_name='Usuario', blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Apertura de puerta"
        verbose_name_plural = "Aperturas de puertas"

    def __str__(self):
        return str(self.user)
