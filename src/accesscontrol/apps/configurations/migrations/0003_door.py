# Generated by Django 2.2 on 2019-05-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0002_entity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_name', models.CharField(max_length=60, verbose_name='Nombre de la puerta')),
            ],
        ),
    ]
