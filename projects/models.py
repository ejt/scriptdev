from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, help_text='Just a few words about the project.')
    url = models.URLField(verify_exists=False, help_text='example: http://site.scriptdev.se')
    img = models.ImageField(upload_to='/WE_NEED_OS_Join_thing_here/', height_field='200', width_field='287')
    def __unicode__(self):
        return self.name

