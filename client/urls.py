from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^', 'client.views.status'),
)
