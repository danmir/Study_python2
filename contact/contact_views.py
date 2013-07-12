__author__ = 'apple'
from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.http import *

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})