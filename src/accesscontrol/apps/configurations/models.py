from django.db import models
from django.contrib import admin
from django.utils.html import format_html


# Create your models here.


class General(models.Model):
    site_name = models.CharField(verbose_name='Nombre del sitio', max_length=60)
    site_image = models.ImageField(verbose_name='Logo', upload_to='configuracion/general/')
    with_image = models.PositiveIntegerField(verbose_name='Ancho del logo', default=100)
    height_image = models.PositiveIntegerField(verbose_name='Alto del logo', default=60)

    class Meta:
        verbose_name = "Configuración general"
        verbose_name_plural = "Configuración general"

    def save(self, *args, **kwargs):
        site_name = self.site_name
        logo_url = "/media/"+str(self.site_image)
        name = format_html("<img src={url} height={h} width={w}><br><h5>"+site_name+"</h5>", url=logo_url, w=self.with_image, h=self.height_image)
        admin.site.site_header = name if site_name else 'Administración del Sistema'
        super(General, self).save(*args, **kwargs)

    def __str__(self):
        return self.site_name

class Entity(models.Model):
    entity_name = models.CharField(verbose_name='Nombre de la entidad', max_length=60)
    entity_image = models.ImageField(verbose_name='Logo', upload_to='configuracion/entity/')

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.entity_name


class Door(models.Model):
    door_name = models.CharField(verbose_name='Nombre de la puerta', max_length=60)

    class Meta:
        verbose_name = "Puerta"
        verbose_name_plural = "Puertas"

    def __str__(self):
        return self.door_name
