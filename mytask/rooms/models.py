from django.db import models
from django.urls import reverse

# Create your models here.

class Insumo(models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingrese nombre")
    
    def __str__(self):

        return self.nombre

class Sala(models.Model):
    nombre = models.CharField(max_length=200, help_text="Introduzca el nombre de la sala")
    ubicacion = models.CharField(max_length=200, help_text="Introduzca ubicación")
    insumo = models.ManyToManyField(Insumo, help_text="Seleccione insumos")
    capacidad = models.IntegerField(default=0)
    hora_disp_ini = models.TimeField(null=True)
    hora_disp_fin = models.TimeField(null=True)

    class Meta:
        ordering = ["nombre"]

    LOAN_STATUS = (
        ('d', 'Disponible'),
        ('n', 'No disponible'),
        ('r', 'Reservada'),
        ('c', 'Confirmada'),
    )

    estado = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Disponibilidad de la sala')
    
    def get_absolute_url(self):
        """
        	Retorna la url para acceder a una instancia particular de una sala.
        """
        return reverse('sala_detail', args=[str(self.id)])

    def __str__(self):

        return self.nombre

class Empleador(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        """
        	Retorna la url para acceder a una instancia particular de un empleador.
        """
        return reverse('empleador-detalle', args=[str(self.id)])

    def __str__(self):

        return '%s, %s' % (self.apellido, self.nombre)

import uuid # instancia de reserva único

class Reserva(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este la reserva")
    sala = models.ForeignKey('Sala', on_delete=models.SET_NULL, null=True) 
    fecha = models.DateField(null=True, blank=True)
    hora_ini = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)
    capacidad = models.IntegerField(default=0)
    empleado = models.ForeignKey('Empleador', on_delete=models.SET_NULL, null=True) 
    insumo = models.ManyToManyField(Insumo, help_text="Seleccione insumos")

    LOAN_STATUS = (
        ('c', 'Confirmada'),
        ('p', 'Pendiente')
    )

    estado = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='p', help_text='Disponibilidad de la sala')

    class Meta:
        ordering = ["fecha"]

    def __str__(self):

        return '%s (%s)' % (self.id,self.sala.nombre)