
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoas/', include('pessoas.urls')),  
    path('depto/', include('depto.urls')),  
    path('salario/', include('salario.urls')),
    path('accounts/', include('django.contrib.auth.urls')) #urls de autenticacao

]
