from django.forms import ModelForm
from django.db import models
from .models import Pessoa


class PessoaForm(ModelForm):
     
     class Meta:
        model = Pessoa
        fields = '__all__'


#aqui vai os froms de adicao dos dados do usuario 
# 3 froms exibir,editar dados, editar senha
# nao jogar os dados direto no model 
# alterar senha deve passar uma verificacao, so o admin ou usuario pode alterar, 
#userchangeform editar 
#para casa criar o form para alterar senha