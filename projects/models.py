from django.db import models
import os

class Image(models.Model):
    title = models.CharField(max_length = 30)
    image = models.ImageField(upload_to=os.path.join('img', 'projects'))

    def __unicode__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, help_text='Just a few words about the project.')
    url = models.URLField(verify_exists=False, help_text='example: http://site.scriptdev.se')
    image = models.ForeignKey(Image)
    sort = models.PositiveIntegerField(help_text='Ordering 1 = top 777 = very low')
    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name
