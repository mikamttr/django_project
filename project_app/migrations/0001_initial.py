# Generated by Django 5.0.1 on 2024-04-06 16:10

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_name', models.CharField(max_length=100)),
                ('leave_description', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Leave_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('delivery_date', models.DateField()),
                ('status', models.CharField(choices=[('paused', 'En pause'), ('planned', 'Planifié'), ('pending', 'En cours'), ('delivered', 'Livré')], default='planned', max_length=20)),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('low', 'Faible'), ('medium', 'Moyenne'), ('high', 'Élevée')], max_length=20)),
                ('start_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('status', models.CharField(choices=[('paused', 'En pause'), ('planned', 'Planifié'), ('ongoing', 'En cours'), ('completed', 'Réalisée'), ('validated', 'Validée')], max_length=20)),
                ('completion_percentage', models.IntegerField(default=0)),
                ('assigned_to', models.ManyToManyField(related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
                ('parent_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_tasks', to='project_app.task')),
                ('progress_reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_reports', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.project')),
            ],
        ),
    ]
