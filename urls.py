from django.conf.urls.defaults import *
import refuge

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^clam/?$', 'visual.views.index'),
    (r'^clam/do_task', 'visual.views.do_task'),
    #(r'^refuge/?', include(refuge.urls)),
    (r'^clam/recur?', 'visual.views.recurring_tasks'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/src/clam/static'}),

    #login
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
