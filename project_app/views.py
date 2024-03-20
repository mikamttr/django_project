from django.shortcuts import render, redirect, get_object_or_404
from project_app.forms import ProjectForm
from project_app.models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after adding the project
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_details.html', {'project': project})
