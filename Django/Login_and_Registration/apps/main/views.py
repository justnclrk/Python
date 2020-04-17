# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import User
import bcrypt
import re


def index(request):
    return render(request, 'main/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        User.objects.create(fname=request.POST["fname"], lname=request.POST["lname"], email=request.POST["email"], password=bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()))
        user = User.objects.last()
        request.session['id'] = user.id
        return redirect('/success')

def login(request):
    try:
        user = User.objects.get(email=request.POST["email"])
    except:
        messages.error(request, "Login Failed, invalid email")
        return redirect('/')

    if bcrypt.checkpw(request.POST["password"].encode(), user.password.encode()):
        request.session["id"] = user.id
        return redirect('/success')
    else:
        messages.error(request, "Login Failed, invalid password")
        return redirect('/')

def success(request):
    user = User.objects.get(id=request.session["id"])
    context = {
        'name': user.fname
    }
    return render(request, 'main/success.html', context)

def log_out(request):
    users = User.objects.all()
    for user in users:
        user.delete()
    return redirect('/')