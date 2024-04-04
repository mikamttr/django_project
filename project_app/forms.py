from django import forms
from .models import Project, Task, User, Leave


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'
