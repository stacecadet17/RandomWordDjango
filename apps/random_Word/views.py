from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if "count" not in request.session:
        request.session['count'] = 0
    if "word" not in request.session:
        request.session['word'] = ""
    return render(request, "random_Word/index.html")

def generate(request):
    request.session['word'] = get_random_string(length=14)
    request.session['count'] += 1
    return redirect('/')

def reset(request):
    del request.session['word']
    del request.session['count']
    return redirect('/')
