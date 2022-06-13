from django.contrib import admin
from .models import Project, Rating


#register class models
admin.site.register(Project)
admin.site.register(Rating)
