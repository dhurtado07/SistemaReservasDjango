from django.db import models
from django.core.exceptions import ValidationError
import datetime

def validate_positive(value):
    if value <= 0:
        raise ValidationError('El valor debe ser mayor que cero.')

def validate_future_date(value):
    if value <= datetime.date.today():
        raise ValidationError('La fecha debe ser en el futuro.')

class Reserva(models.Model):
    fecha = models.DateField(validators=[validate_future_date])
    cantidad_personas = models.IntegerField(validators=[validate_positive])

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, validators=[validate_positive])

class Meta:
        app_label = 'reservas_app'