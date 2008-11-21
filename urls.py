from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('comtwitter.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),

    # Serving static files
    (r'^update/(?P<status>.*)$', 'comtwitter.views.update'),
    (r'^show/(?P<status>\w+)$', 'comtwitter.views.show'),
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_DIR+'/files'}),
)
