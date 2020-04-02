# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'users/index.html', { "Users": User.objects.all() })

def show(request, id):
    user = User.objects.get(id = id)
    context = {
        'user': user
    }
    return render(request, 'users/user_page.html', context)

def new(request):
    return render(request, 'users/add_user.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:   
        User.objects.create(full_name=request.POST["full_name"], email=request.POST["email"])
        return redirect('/users')

def edit(request, id):
    user = User.objects.get(id = id)
    context = {
        'user': user
    }
    return render(request, 'users/edit_user.html', context)

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/user/+id/edit')
    else:
        user = User.objects.get(id = id)
        user.full_name = request.POST['full_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users')

def delete(request, id):
    b = User.objects.get(id = id)
    b.delete()
    return redirect('/users')