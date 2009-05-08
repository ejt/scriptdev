from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Index
    (r'^$', 'scriptdev.views.index'),

    # Log in / Log out
    (r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'index.html'
    }),
    (r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/',
    }),

    # Admin
    (r'^admin/(.*)', admin.site.root),
)

import os
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': os.path.join(settings.PROJECT_PATH, 'media'),
        }),
    )
