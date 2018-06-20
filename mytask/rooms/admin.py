from django.contrib import admin
from .models import Insumo, Sala, Empleador, Reserva

# Register your models here.

admin.site.register(Insumo)
admin.site.register(Sala)
admin.site.register(Empleador)
admin.site.register(Reserva)