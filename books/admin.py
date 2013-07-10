#-*- coding: utf-8 -*-
from django.contrib import admin
from books.models import Publisher, Author, Book

#Для отображения в admin панели
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)  #'-' В порядке убывания
    #Порядок следования в форме редактирования
    fields = ('title', 'authors', 'publisher', 'publication_date')
    #Только для полей Manytomany удобное добавление
    filter_horizontal = ('authors',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)