from django.contrib import admin

from project_app.models import User, Task, Project

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
