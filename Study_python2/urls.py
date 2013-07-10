from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from Study_python2.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^$', myHomePageView),
    (r'^time/plus/(\d{1,2})/$', hoursAhead),
    (r'^ua/$', ua_display),
    # Examples:
    # url(r'^$', 'Study_python2.views.home', name='home'),
    # url(r'^Study_python2/', include('Study_python2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
