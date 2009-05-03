from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):
    user = models.ForeignKey(User, unique = True, verbose_name = _('user'))
    roles = models.CharField(_('roles'), max_length = 50, blank = True, help_text = _('Member roles, eg. "Programmer, Webdesigner"'))
    twitter_username = models.CharField(_('twitter username'), max_length = 15, blank = True, help_text = _('Enter username to display latest tweet on the front page'))

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __unicode__(self):
        return '%s\'s profile' % self.user

# Signal handler that creates a profile for each user that gets created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile(user = instance).save()
models.signals.post_save.connect(create_profile, sender = User)
