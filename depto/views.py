from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Depto
from .forms import DeptoForm

def depto_list(request):
    departamentos = Depto.objects.all()
    return render(request, 'depto/depto_list.html', {'departamentos': departamentos})

#cria um novo registro

def add(request):
    print("entrou def")
    if request.method == 'POST':
        form = DeptoForm(request.POST)
        if form.is_valid():
            form.save()
            print("chegou")
            return HttpResponseRedirect('/depto/')
    else:
        form = DeptoForm()
   
    
    print("chegou aqui")
    return render(request, 'depto/form.html', {'form':form})

def editar_depto(request, id):  
    depto = get_object_or_404(Depto, pk=id)
    if request.method == 'POST':
        form = DeptoForm(request.POST, instance=depto)  
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/depto/')
    else:
        form = DeptoForm(instance=depto)
    return render(request, 'depto/form.html', {'form': form})


def depto_detail(request, pk):
    depto = get_object_or_404(Depto, pk=pk)
    return render(request, 'depto/depto_detail.html', {'depto': depto})


