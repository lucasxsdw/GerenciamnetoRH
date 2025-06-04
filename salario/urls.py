from django.urls import path
from . import views

urlpatterns = [
    path('', views.salario_list, name='salario_list'),
    path('addSalario/', views.add_salario, name='forms'),
    path('editarSalario/<int:id>', views.editar_salario, name='editar'),
    path('excluirSalario/<int:id>', views.excluir_salario, name='excluir_salario'),
     path('salario/<int:pk>/', views.salario_detail, name='salario_detail')  # Adicionada esta linha
 

]
    