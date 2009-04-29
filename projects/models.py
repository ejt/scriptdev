from django.db import models

# Create your models here.

class OurProjects(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=30)
    project_url = models.CharField(max_length=30)
    def __unicode__(self):
        return self.project_name

