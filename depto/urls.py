from django.urls import path
from . import views

urlpatterns = [
    path('', views.depto_list, name='depto_list'),
    path('<int:pk>/', views.depto_detail, name='depto_detail'),
    path('add/', views.add, name='formulario'),
    path('editar/<int:id>', views.editar_depto, name='depto')


]
