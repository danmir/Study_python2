# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from books.models import Book
# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        #Получить книги, название которых содержит q без учета регистра
        books = Book.objects.filter(title__icontains = q)
        return render_to_response('search_result.html', {'books' : books, 'query' : q})
    else:
        return HttpResponse('Введите новый поисковый запрос')