from itertools import groupby
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from authentification.forms import UserForm
from django.contrib.auth.models import Group
from project_app.forms import ProjectForm, TaskForm, LeaveForm
from project_app.models import Project, User, Task, Leave
from project_app.utils import gantt_chart


@login_required
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


@login_required
@permission_required('project_app.add_project')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after adding the project
    else:
        form = ProjectForm()
        # Fetch users with role "manager"
        managers = User.objects.filter(user_role=User.MANAGER)
    return render(request, 'project/add_project.html', {'form': form, 'managers': managers})


@login_required
@permission_required('project_app.view_project')
def project_details(request, project_id):
    gantt, max_end_date = gantt_chart(project_id)
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.task_set.all().order_by('parent_task_id')  # Ensure tasks are ordered by parent task
    grouped_tasks = {}

    for parent_task, task_group in groupby(tasks, key=lambda x: x.parent_task):
        if parent_task is not None:
            grouped_tasks[parent_task] = list(task_group)
        else:
            grouped_tasks["None"] = list(task_group)

    return render(request, 'project/project_details.html', {
        'project': project,
        'grouped_tasks': grouped_tasks,
        'gantt_chart': gantt,
        'max_end_date': max_end_date
    })


@login_required
@permission_required('project_app.change_project')
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_details', project_id=project_id)
    else:
        form = ProjectForm(instance=project)
        managers = User.objects.filter(user_role='manager')
    return render(request, 'project/edit_project.html', {'form': form, 'managers': managers})


@login_required
@permission_required('project_app.delete_project')
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('home')


@login_required
@permission_required('project_app.view_task')
def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task/task_details.html', {'task': task})


@login_required
@permission_required('project_app.add_task')
def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    main_tasks = Task.objects.filter(parent_task__isnull=True)
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

    # Fetch all tasks related to the project
    parent_tasks = Task.objects.filter(project=project)

    return render(request, 'task/add_task.html',
                  {'form': form, 'project_id': project_id, 'parent_tasks': parent_tasks, 'main_tasks': main_tasks})


@login_required
@permission_required('project_app.change_project')
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    main_tasks = Task.objects.filter(parent_task__isnull=True)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_details', task_id=task_id)
    else:
        form = TaskForm(instance=task)

    # Fetch all users who can be assigned to the task
    users = User.objects.all()

    # Fetch all projects
    projects = Project.objects.all()

    # Fetch all tasks of the current viewed task's project
    project_tasks = Task.objects.filter(project=task.project)

    # Pass all necessary values to the template context
    context = {
        'form': form,
        'task': task,
        'users': users,  # Include all users in the context
        'projects': projects,  # Include all projects in the context
        'project_tasks': project_tasks,
        'main_tasks': main_tasks  # Include all tasks of the current viewed task's project in the context
    }

    # Render the edit_task.html template with the context
    return render(request, 'task/edit_task.html', context)


@login_required
@permission_required('project_app.delete_task')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        # Redirect the user to the project details page after deletion
        return redirect('project_details', project_id=task.project.id)


@login_required
def user_home(request):
    users = User.objects.all()
    return render(request, 'user/user.html', {'users': users})


@login_required
@permission_required('authentification.add_user')
def add_user(request):
    roles = User.ROLE_CHOICES
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            email = form.data.get('email')
            user_role = form.data.get('user_role')
            user = User.objects.create_user(username=username, password=password, email=email, user_role=user_role)
            user.save()
            group_name = form.data.get('user_role')
            group = Group.objects.get(name=group_name.lower())
            group.user_set.add(user)
            return redirect('home_user')
    else:
        form = UserForm()
    return render(request, 'user/add_user.html', {'form': form, 'roles': roles})


@login_required
@permission_required('authentification.view_user')
def user_details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/user_details.html', {'user': user})


@login_required
@permission_required('authentification.delete_user')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('home_user')


@login_required
@permission_required('project_app.add_leave')
def add_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.save()
            return redirect('home_leave')
    else:
        form = LeaveForm()
        users = User.objects.all()
    return render(request, 'leaves/add_leave.html', {'form': form, 'users': users})


@login_required
@permission_required('project_app.view_leave')
def home_leave(request):
    leaves = Leave.objects.all()
    return render(request, 'leaves/leaves.html', {'leaves': leaves})


@login_required
@permission_required('project_app.view_leave')
def leave_details(request, leave_id):
    # Récupérer le congé spécifique en fonction de l'ID
    leave = get_object_or_404(Leave, pk=leave_id)
    # Rendre le template avec le congé spécifique
    return render(request, 'leaves/leave_details.html', {'leave': leave})


@login_required
@permission_required('project_app.delete_leave')
def delete_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    if request.method == 'POST':
        leave.delete()
        return redirect('home_leave')
    return render(request, 'leaves/leave_details.html', {'leave': leave})

