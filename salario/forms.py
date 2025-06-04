from django.forms import ModelForm
from django.db import models
from .models import Salario


class SalarioForm(ModelForm):
     
     class Meta:
        model = Salario
        fields = '__all__'