from django.db import models
from pessoas.models import Pessoa



class Salario(models.Model):
    pessoa = models.ManyToManyField(Pessoa)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.salario}"
