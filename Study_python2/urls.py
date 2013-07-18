# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls import patterns, include, url
from Study_python2.views import *
from django.views.generic import list
from books import views
from books.models import Publisher
#Для Generetic view
from views import PublisherList
#Для login logout
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html',
}

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^$', myHomePageView),
    (r'^time/plus/(\d{1,2})/$', hoursAhead),
    (r'^ua/$', ua_display),
    (r'^display_meta/$', display_meta),
    #Форма поиска
    (r'^search/$', views.search),
    #Контактная форма
    (r'^contact/$', 'contact.contact_views.contact'),
    #Именованные группы
    (r'^problem/(?P<num>\d{1,2})/$', problem),
    #Автоматические страницы
    url(r'^publishers/$', PublisherList.as_view()),
    #Авторизация
    (r'^session/$', session),
    (r'^sessioncheck/$', checkSession),
    (r'^login/$', login, {'template_name': 'login.html'}),
    (r'^logout/$', logout, {'template_name': 'logout.html'}),
    # Examples:
    # url(r'^$', 'Study_python2.views.home', name='home'),
    # url(r'^Study_python2/', include('Study_python2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)