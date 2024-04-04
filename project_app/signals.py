from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task, Project

@receiver(post_save, sender=Task)
@receiver(post_delete, sender=Task)
def update_project_status_and_progress(sender, instance, **kwargs):
    project = instance.project

    # Update project status
    all_tasks_validated = all(task.status == 'validated' for task in project.task_set.all())
    if all_tasks_validated:
        project.status = 'delivered'
    else:
        project.status = 'planned'
    project.save()

    # Update project progress percentage
    total_tasks = project.task_set.count()
    if total_tasks > 0:
        total_completion = sum(task.completion_percentage for task in project.task_set.all())
        project.progress_percentage = total_completion / total_tasks
    else:
        project.progress_percentage = 0
    project.save()

@receiver(post_save, sender=Task)
def update_project_status_on_task_update(sender, instance, **kwargs):
    # check if all task are validated
    project = instance.project
    all_tasks_validated = all(task.status == 'validated' for task in project.task_set.all())
    if all_tasks_validated:
        # set project status to delivered
        project.status = 'delivered'
        project.save()
