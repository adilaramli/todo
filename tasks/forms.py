from dataclasses import field
from socket import fromshare
from django import forms
from django.forms import ModelForm

from .models import *

#create model form

class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

    
    class Meta:
        model = Task
        fields = '__all__'