# Generated by Django 2.2 on 2019-05-01 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0003_door'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='door',
            options={'verbose_name': 'Puerta', 'verbose_name_plural': 'Puertas'},
        ),
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='general',
            options={'verbose_name': 'Configuración general', 'verbose_name_plural': 'Configuración general'},
        ),
    ]