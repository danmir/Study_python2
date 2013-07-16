# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

__author__ = 'apple'

def hello(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
    #html = "<html><body>Сейчас {} </body></html>".format(now) #1 версия
    #t = get_template('current_datetime.html') #2 версия
    #html = t.render(Context({'current_date': now})) #2 версия
    #return HttpResponse(html) #2 версия

def myHomePageView(request):
    return HttpResponse("My Home page")

def hoursAhead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    #assert False
    html = "<html><body>Через {} часов будет {}.</body></html>".format(offset, dt)
    return HttpResponse(html)

def ua_display(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse('Ваш броузер {}'.format(ua))

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for key, value in values:
        html.append('<tr><td>{}</td><td>{}</td></tr>'.format(key, value))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def problem(request, num):
    return HttpResponse('Id задлачи {}'.format(num))