# -*- coding: utf-8 -*-
__author__ = 'apple'
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Ваш e-mail')
    message = forms.CharField()

    #Вызывается после стандартных проверок
    def clean_message(self):
        #О том что в поле не пусто позаботился стандартный обработчик
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Слишком мало слов')
        return message