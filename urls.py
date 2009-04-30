from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^scriptdev/', include('scriptdev.foo.urls')),

    # Django Admin
    (r'^admin/(.*)', admin.site.root),
    
    # Login
    (r'^login/$', 'django.contrib.auth.views.login'),
)

import os
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': os.path.join(settings.PROJECT_PATH, 'media'),
        }),
    )
