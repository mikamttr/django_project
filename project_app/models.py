from django.db import models
from django.utils import timezone


class User(models.Model):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user_role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password = models.CharField(max_length=255, default='123')

    def __str__(self):
        return self.username


class Task(models.Model):
    STATUS_CHOICES = (
        ('paused', 'En pause'),
        ('planned', 'Planifié'),
        ('ongoing', 'En cours'),
        ('completed', 'Réalisée'),
        ('validated', 'Validée'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Faible'),
        ('medium', 'Moyenne'),
        ('high', 'Élevée'),
    )

    task_name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    start_date = models.DateField()
    duration = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    completion_percentage = models.IntegerField(default=0)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    progress_reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_reports')
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_tasks')

    def __str__(self):
        return self.task_name


class Project(models.Model):
    STATUS_CHOICES = (
        ('paused', 'En pause'),
        ('planned', 'Planifié'),
        ('pending', 'En cours'),
        ('delivered', 'Livré'),
    )

    project_name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    progress_percentage = models.IntegerField(default=0)
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_managed')

    def __str__(self):
        return self.project_name
