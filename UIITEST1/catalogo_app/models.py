from django.db import models

class Catalogo(models.Model):
    id_catalogo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=6)
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio", null=False, blank=False)
    fecha_fin = models.DateField(verbose_name="Fecha de fin", null=False, blank=False)
    promocion = models.CharField(max_length=100)
    colecciones = models.CharField(max_length=50)
    novedades = models.CharField(max_length=75)  # Corrección aquí

    def __str__(self) -> str:
        return self.nombre
