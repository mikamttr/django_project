from django.urls import path
from . import views
from .views import connexion, logout_user

urlpatterns = [
    path('', views.home, name='home'),
    path('connexion/', connexion, name='connexion'),
    path('logout/', logout_user, name='logout'),
    path('users/', views.user_home, name='home_user'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/<int:user_id>/', views.user_details, name='user_details'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:project_id>/', views.project_details, name='project_details'),
    path('projects/edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:project_id>/add_task/', views.add_task_to_project, name='add_task_to_project'),
    path('leaves/add/', views.add_leave, name='add_leave'),
    path('leaves/', views.home_leave, name='home_leave'),
    path('task/<int:task_id>/', views.task_details, name='task_details'),
    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]
