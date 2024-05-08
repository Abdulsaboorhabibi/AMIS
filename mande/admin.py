from django.contrib import admin
from .models import ProjectModel, MonitorProjectModel

admin.site.register(ProjectModel)
admin.site.register(MonitorProjectModel)