# Generated by Django 2.2 on 2019-05-01 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190501_0159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil de usuario', 'verbose_name_plural': 'Perfiles de usuarios'},
        ),
    ]