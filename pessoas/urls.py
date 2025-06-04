from django.urls import path
from . import views

urlpatterns = [
    path('', views.pessoa_list, name='pessoa_list'),
    path('<int:pk>/', views.pessoa_detail, name='pessoa_detail'),
    path('add/', views.add, name='form'),
    path('editar/<int:id>', views.editar_pessoa, name='editar'),
    path('excluir/<int:id>', views.excluir_pessoa, name='excluir_pessoa')


]
