from django import forms
from .models import Pessoa, Salario

class PessoaForm(forms.ModelForm):
    salario = forms.ModelChoiceField(queryset=Salario.objects.all(), required=True)
    ano = forms.IntegerField(required=True)
    mes = forms.IntegerField(required=True)

    class Meta:
        model = Pessoa
        fields = ['nome', 'cargo', 'departamento', 'data_contratacao']



#aqui vai os froms de adicao dos dados do usuario 
# 3 froms exibir,editar dados, editar senha
# nao jogar os dados direto no model 
# alterar senha deve passar uma verificacao, so o admin ou usuario pode alterar, 
#userchangeform editar 
#para casa criar o form para alterar senha