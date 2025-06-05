from django.db import models




class Salario(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="valor")
    anos_trabalho = models.PositiveSmallIntegerField(verbose_name=" Anos de trabalho")
   
    def __str__(self):
        return f'{self.valor} - {self.anos_trabalho} anos de trabalho'
