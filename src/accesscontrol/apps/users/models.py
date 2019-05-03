from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    def  __str__(self):
        return self.first_name+" "+self.last_name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(verbose_name='Imagen de perfil', upload_to='profiles/', null=True, blank=True)
    first_name = models.CharField(verbose_name='Nombres', max_length=100)
    last_name = models.CharField(verbose_name='Apellidos', max_length=100)
    id_card = models.CharField(verbose_name='Cédula', max_length=10)
    id_card_rfid = models.CharField(verbose_name='Código de tarjeta RFID', max_length=10, default=0)
    entities = models.ManyToManyField('configurations.Entity', verbose_name="Empresas")

    class Meta:
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuarios"

    def  __str__(self):
        return self.first_name+" "+self.last_name
