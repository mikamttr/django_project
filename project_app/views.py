from django.shortcuts import render, redirect, get_object_or_404
from project_app.forms import ProjectForm, TaskForm, UserForm
from project_app.models import Project, User


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


def add_task_to_project(request, project_id):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project_id = project_id
            task.save()
            return redirect('project_detail', project_id=project_id)
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def user_home(request):
    users = User.objects.all()
    return render(request, 'user/user.html', {'users': users})


def add_user(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
        roles = User.ROLE_CHOICES
    return render(request, 'user/add_user.html', {'form': form, 'roles': roles})


def user_details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/user_details.html', {'user': user})
