# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from books.models import Book
# Create your views here.

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains = q)
            return  render_to_response('search_result.html', {'books' : books, 'query' : q})
    return render_to_response('search_form.html', {'error' : error})