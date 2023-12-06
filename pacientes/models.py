from django.db import models

class Soldado(models.Model):
    GRADO_CHOICES = [
        ('R', 'Recluta'),
        ('S', 'Soldado'),
        ('C', 'Cabo'),
        ('Sgto', 'Sargento'),
        # Agregar más opciones según sea necesario
    ]

    nombre = models.CharField(max_length=100)
    rango = models.CharField(max_length=10, choices=GRADO_CHOICES)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    unidad = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    grupo_sanguineo = models.CharField(max_length=5)
    alergias = models.TextField(blank=True, null=True)
    condiciones_medicas = models.TextField(blank=True, null=True)