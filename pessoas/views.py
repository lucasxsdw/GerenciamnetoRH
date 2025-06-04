from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm
from django.contrib import messages

def pessoa_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/pessoa_list.html', {'pessoas': pessoas})
#cria um novo registro

def add(request):
    print("entrou def")
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            print("chegou")
            return HttpResponseRedirect('/pessoas/')
    else:
        form = PessoaForm()
   
    
    print("chegou aqui")
    return render(request, 'pessoas/form.html', {'form':form})

def editar_pessoa(request):
    pessoa = Pessoa.objects.get(pk=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=Pessoa)
        if form.is_valid():
            form.save()
            print("chegou")
            return HttpResponseRedirect('/pessoas/')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoas/form.html', {'form':form})
    
def excluir_pessoa(request, id):
    if request.method == 'POST':
        try:
            excluirPessoa = Pessoa.objects.get(pk=id)
            excluirPessoa.delete()
            messages.success(request, "Salario excluída com sucesso!")
            return render(request, 'pessoas/pessoa_detail.html', {'pessoa': excluirPessoa})
        except Pessoa.DoesNotExist:
            print("pessoa nao existe ")
    else:
        print("FOI GET")


def pessoa_detail(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    return render(request, 'pessoas/pessoa_detail.html', {'pessoa': pessoa})
