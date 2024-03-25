from django.shortcuts import render, redirect, get_object_or_404
from project_app.forms import ProjectForm, TaskForm
from project_app.models import Project, User, Task


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
        # Fetch users with role "manager"
        managers = User.objects.filter(user_role='manager')
    return render(request, 'add_project.html', {'form': form, 'managers': managers})


def project_details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.task_set.all()  # Retrieve all tasks associated with this project
    return render(request, 'project_details.html', {'project': project, 'tasks': tasks})


def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_details.html', {'task': task})


def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project  # Assign the project manually
            task.save()
            return redirect('project_details', project_id=project_id)
        else:
            print(form.errors)  # Print form errors to console
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form, 'project_id': project_id})