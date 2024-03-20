from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'start_date', 'delivery_date', 'status', 'progress_percentage', 'project_manager']
