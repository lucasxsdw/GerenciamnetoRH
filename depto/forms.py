from django.forms import ModelForm
from django.db import models
from .models import Depto


class DeptoForm(ModelForm):
     
     class Meta:
        model = Depto
        fields = '__all__'