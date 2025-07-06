from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from salario.models import Salario
from .models import Pessoa, PessoaSalario
from .forms import PessoaForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import PessoaSalario

@login_required
def pessoa_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/pessoa_list.html', {'pessoas': pessoas})
#cria um novo registro


@permission_required('pessoas.add_pessoa', raise_exception=True)
@login_required
def add(request):
    form = PessoaForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        pessoa = form.save()
        PessoaSalario.objects.create(
            pessoa=pessoa,
            salario=form.cleaned_data['salario'],
            ano=form.cleaned_data['ano'],
            mes=form.cleaned_data['mes']
        )
        return redirect('/pessoas/')
    
    return render(request, 'pessoas/form.html', {'form': form})





@permission_required('pessoas.change_pessoa', raise_exception=True)
@login_required
def editar_pessoa(request, id):  
    pessoa = get_object_or_404(Pessoa, pk=id)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)  
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoas/')
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'pessoas/form.html', {'form': form})



@permission_required('pessoas.delete_pessoa', raise_exception=True)
@login_required 
def excluir_pessoa(request, id):
    if request.method == 'POST':
        try:
            excluirPessoa = Pessoa.objects.get(pk=id)
            excluirPessoa.delete()
            messages.success(request, "Salario excluída com sucesso!")
            return render(request, 'pessoas/pessoa_list.html', {'pessoa': excluirPessoa})
        except Pessoa.DoesNotExist:
            print("pessoa nao existe ")
    else:
        print("FOI GET")

@login_required
def pessoa_detail(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    return render(request, 'pessoas/pessoa_detail.html', {'pessoa': pessoa})
