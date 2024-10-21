from django import forms
from .models import Corse, Material

class CorseForm(forms.ModelForm):
    class Meta:
        model = Corse
        fields = ['titel', 'description']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['corse','title','file']