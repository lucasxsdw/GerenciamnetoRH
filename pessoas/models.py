from django.db import models


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
class Pessoa(models.Model):
    nome = models.CharField(max_length=100) 
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    valor_salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_contratacao = models.DateField()
    

    def __str__(self):
        return self.nome    
    
