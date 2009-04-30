from django.db import models

# Create your models here.

class OurProjects(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=30, help_text='Just a few words about the project.')
    project_url = models.CharField(max_length=30, help_text='example: http://site.scriptdev.se')
    def __unicode__(self):
        return self.project_name

