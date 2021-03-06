from django.contrib import admin
from models import Project, Image

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url', 'sort')

admin.site.register(Image)
admin.site.register(Project, ProjectAdmin)
