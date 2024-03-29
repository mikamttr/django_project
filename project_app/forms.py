from django import forms
from .models import Project, Task, Leave

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'start_date', 'delivery_date', 'status', 'progress_percentage', 'project_manager']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'priority', 'start_date', 'duration', 'assigned_to', 'progress_reporter']

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['leave_name', 'leave_description', 'start_date', 'end_date', 'user_id']
