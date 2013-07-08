#-*- coding: utf-8 -*-
from django.contrib import admin
from books.models import Publisher, Author, Book

#Для отображения в admin панели
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)