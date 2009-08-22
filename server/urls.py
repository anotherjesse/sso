from django.conf.urls.defaults import *
from wapi.bindings import RestBinding
from api import UserApi
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'server.views.status'),
    (r'^login/$', 'server.views.login'),
    (r'^logout/$', 'server.views.logout'),
    (r'^admin/(.*)', admin.site.root),
    (r'^api/%s$' % RestBinding.PATTERN, RestBinding(api=UserApi())),
)
