
from django.db import models

# Create your models here.

class inventario(models.Model):
    id_inventario = models.CharField(primary_key=True,max_length=6)
    kilos_de_carne = models.CharField(max_length=100)
    tipos_de_carne = models.PositiveSmallIntegerField()
    tipos_de_salsa = models.PositiveSmallIntegerField()
    tortillas = models.PositiveSmallIntegerField()
    verduras = models.PositiveSmallIntegerField()
    desechables = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.id_inventario