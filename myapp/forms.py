from django import forms
from .models import Unnes

class UnnesForm(forms.ModelForm):
    class Meta:
        model = Unnes     #создание формы под модель
        fields = [
            'title',
            'description',
            'price',
        ]
