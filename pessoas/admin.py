from django.contrib import admin

from django.contrib import admin
from .models import Pessoa, Departamento, Cargo

admin.site.register(Pessoa)
admin.site.register(Departamento)
admin.site.register(Cargo)

