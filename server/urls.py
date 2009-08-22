from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'server.views.status'),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'server.views.logout'),
    (r'^admin/(.*)', admin.site.root),
)
