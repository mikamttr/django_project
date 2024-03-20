from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:project_id>/', views.project_details, name='project_details'),
]
