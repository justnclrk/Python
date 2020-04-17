# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
def index(request, methods="POST"):
    return render (request, 'index.html')

def process(request):
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["lang"] = request.POST["lang"]
    request.session["comm"] = request.POST["comm"]
    return redirect('/results')

def results(request):
    return render (request, 'results.html')

def goback(request, methods="GET"):
    return redirect('/')