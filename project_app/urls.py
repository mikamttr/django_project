from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:project_id>/', views.project_details, name='project_details'),
    path('task/<int:task_id>/', views.task_details, name='task_details'),
    path('project/<int:project_id>/add_task/', views.add_task_to_project, name='add_task_to_project'),
]
