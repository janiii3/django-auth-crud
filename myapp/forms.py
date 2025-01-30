from django import forms
from django.forms import ModelForm
from .models import Task2, Task

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo de tarea', max_length=200)
    description = forms.CharField(label='Descripcion de tarea', widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del proyecto', max_length=200)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task2
        fields = ['title', 'description', 'importance', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un título'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripción'}),
            'importance': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }
    