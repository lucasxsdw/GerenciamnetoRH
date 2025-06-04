from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Salario
from .forms import SalarioForm
from django.contrib import messages

def salario_list(request):
    salario = Salario.objects.all()
    return render(request, 'salario/salario_list.html', {'salario': salario})
#cria um novo registro


def salario_list(request):
    salarios = Salario.objects.all()
    return render(request, 'salario/salario_list.html', {'salarios': salarios})

def add_salario(request):
 
    if request.method == 'POST':
        form = SalarioForm(request.POST)
        if form.is_valid():
            form.save()
            print("chegou")
            return HttpResponseRedirect('/salario/')
    else:
        form = SalarioForm()
   
    
    return render(request, 'salario/form.html', {'form':form})

def editar_salario(request, id):
    salario_instance = get_object_or_404(Salario, pk=id)
    if request.method == 'POST':
        form = SalarioForm(request.POST, instance=salario_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/salario/')
    else:
        form = SalarioForm(instance=salario_instance)
    return render(request, 'salario/form.html', {'form':form})
    
def excluir_salario(request, id):
    salario_instance = get_object_or_404(Salario, pk=id)
    if request.method == 'POST':
        salario_instance.delete()
        messages.success(request, "Salário excluído com sucesso!")
        return HttpResponseRedirect('/salario/')
    else:
        return render(request, 'salario/confirmar_exclusao.html', {'salario': salario_instance})


def salario_detail(request, pk):
    salario_instance = get_object_or_404(Salario, pk=pk)
    return render(request, 'salario/salario_detail.html', {'salario': salario_instance})
