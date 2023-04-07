from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image' ,'demo_link','description','source_link','tags']
        widgets={'tags': forms.CheckboxSelectMultiple(),}