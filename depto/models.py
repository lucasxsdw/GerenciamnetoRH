from django.db import models


class Depto(models.Model):
    nome = models.CharField(max_length=100)
   

    def __str__(self):
        return self.nome

 #O erro Reverse for 'depto_detail' with arguments '('',)' not found indica que o Django está tentando gerar uma URL para a view depto_detail, que requer um parâmetro pk   
    #def get_absolute_url(self): #isso evita esse erros 
       # return reverse('depto_detail', kwargs={'pk': self.pk})