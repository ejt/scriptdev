from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, unique = True)
    roles = models.CharField(max_length = 50, blank = True, help_text = 'Member roles, separated by spaces, eg. "programmer designer"')
    twitter_username = models.CharField(max_length = 15, blank = True, help_text = 'Enter username to display latest tweet on the front page')

    def __unicode__(self):
        return '%s\'s profile' % self.user

# Signal handler that creates a profile for each user that gets created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile(user = instance).save()
models.signals.post_save.connect(create_profile, sender = User)
