from django.contrib import admin
from django.urls import include, path

import authentification

urlpatterns = [
    path('', include("project_app.urls")),
    path('admin/', admin.site.urls),
]
