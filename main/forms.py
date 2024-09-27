from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList 
from .models import Sotrudnic,Task

class SotrudnicForm(forms.ModelForm):
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.fields['jod'].empty_label = 'Не выбранно'

    class Meta:
        model = Sotrudnic
        fields = ('img','name','email','jod',)
        labels = {
            "jod": ("должность"),
        }
        widgets = {
            'name':forms.TextInput(attrs={'calass':'input-name'}),
            'email':forms.TextInput(attrs={'calass':'input-name'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('img','name','description','who_develops','date_end')


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('img','name','description','who_develops','date_end')

        widgets = {
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': '5'}),
            'who_develops': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'date_end': forms.DateInput(attrs={'class': 'form-control'}),
        }