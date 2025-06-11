from django.db import models
from salario.models import Salario



#criando um relacionamento muitos para um 
class Departamento(models.Model):
    nome =  models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

#uma pessoa esta associada a um departamento e um cargo  e departamento e cargo esta associado a varias pessoas    
# aqui usa ManyToManyField com o modelo Salario, através da tabela intermediaria PessoaSalario.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100) 
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    salario = models.ManyToManyField(Salario, through='PessoaSalario')  
    data_contratacao = models.DateField()
    


    def __str__(self):
        return self.nome    
    
class PessoaSalario(models.Model):
    pessoa = models.ForeignKey(Pessoa, verbose_name="Pessoa", on_delete=models.CASCADE)
    salario = models.ForeignKey(Salario, verbose_name="Salário", on_delete=models.CASCADE)
    ano = models.SmallIntegerField(null=True, blank=True)
    mes = models.SmallIntegerField(verbose_name="Mes")

  # o UniqueConstraint garante que a pessoa nao possa ter 2 salario no mesmo mes, evita duplicidade
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['pessoa', 'ano', 'mes'], name='unique_salario_mensal')
        ]