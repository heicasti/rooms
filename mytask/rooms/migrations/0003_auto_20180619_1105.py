# Generated by Django 2.0.6 on 2018-06-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20180619_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='estado',
            field=models.CharField(blank=True, choices=[('d', 'Disponible'), ('n', 'No disponible'), ('r', 'Reservada'), ('c', 'Confirmada')], default='d', help_text='Disponibilidad de la sala', max_length=1),
        ),
    ]
