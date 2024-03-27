from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_project'),
    path('users', views.user_home, name='home_user'),
    path('users/add/', views.add_user, name='add_user'),
    path('projects/<int:user_id>/', views.user_details, name='user_details'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:project_id>/', views.project_details, name='project_details'),
    path('project/<int:project_id>/add_task/', views.add_task_to_project, name='add_task_to_project'),
]
