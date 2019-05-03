# Generated by Django 2.2 on 2019-05-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_card',
            field=models.CharField(default=1, max_length=10, verbose_name='Cédula'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='id_card_rfid',
            field=models.CharField(default=1, max_length=10, verbose_name='Código de tarjeta RFID'),
            preserve_default=False,
        ),
    ]
