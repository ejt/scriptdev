from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, help_text='Just a few words about the project.')
    url = models.URLField(verify_exists=False, help_text='example: http://site.scriptdev.se')
#    project_img = models.ImageField()
    def __unicode__(self):
        return self.name

