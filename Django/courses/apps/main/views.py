# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

def index(request):
    return render(request, 'main/index.html', { "Courses": Course.objects.all() })

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        Course.objects.create(name=request.POST["name"], desc=request.POST["desc"])
        return redirect('/')

def destroy(request, id):
    b = Course.objects.get(id = id)
    b.delete()
    return redirect('/')

def delete_course(request, id):
    course = Course.objects.get(id = id)
    context = {
        'course': course
    }
    return render(request, 'main/delete.html', context)