from django.conf.urls.defaults import *
import refuge

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^yak/?$', 'visual.views.index'),
    (r'^yak/do_task', 'visual.views.do_task'),
    #(r'^refuge/?', include(refuge.urls)),
    (r'^yak/recur?', 'visual.views.recurring_tasks'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/src/yak/static'}),

    #login
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),


    # yak -- the people indexer
    (r'^people/?', 'yak.people.views.allpeople'),
    (r'^notes/?', 'yak.people.views.allnotes'),
    (r'^tags/?', 'yak.people.views.alltags'),
    (r'^tags/?', 'yak.people.views.alltags'),
    #(r'^people/', include('yak.people.urls')),
    (r'^person/(?P<id>\d+)/?$', 'yak.people.views.person'),
    (r'^note/(?P<id>\d+)/?$', 'yak.people.views.note'),
    (r'^tag/(?P<text>.*)/?$', 'yak.people.views.tag'),
 
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
