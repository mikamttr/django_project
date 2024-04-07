
from django.db import models
from django.utils import timezone
from authentification.models import User



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
    depend_on = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='dependent_tasks')


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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='planned')  # status par défault sur "planifié" à la création
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_manager')

    def __str__(self):
        return self.project_name


class Leave(models.Model):
    leave_name = models.CharField(max_length=100)
    leave_description = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='FK_Leave_user_id')

    def __str__(self):
        return self.leave_name
