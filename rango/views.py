from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dictionary = {'boldmessage': 'This is a bold message'}
    return render(request, 'rango/index.html', context_dictionary)


def about(request):
    context_dictionary = {'italicmessage': 'This is an italic message'}
    return render(request, 'rango/about.html', context_dictionary)