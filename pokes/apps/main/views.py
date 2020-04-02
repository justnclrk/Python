# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Poke
import bcrypt
import re

def index(request):
    if 'id' in request.session:
        return redirect('/pokes')
    else:
        return render(request, 'main/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/main')
    else:
        User.objects.create(name=request.POST["name"], alias=request.POST["alias"], email=request.POST["email"], password=bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()), dob=request.POST["dob"])
        user = User.objects.last()
        request.session['id'] = user.id
        return redirect('/pokes')

def login(request):
    try:
        user = User.objects.get(alias=request.POST["alias"])
    except:
        messages.error(request, "Login Failed, invalid alias")
        return redirect('/main')

    if bcrypt.checkpw(request.POST["password"].encode(), user.password.encode()):
        request.session["id"] = user.id
        return redirect('/pokes')
    else:
        messages.error(request, "Login Failed, invalid password")
        return redirect('/main')

def pokes(request):
    if 'id' not in request.session:
        return redirect('/main')
    else:
        user = request.session['id']
        context = {
            'session_name' : User.objects.get(id=user),
            'people_poked_user' : Poke.objects.filter(poked_user_id=user).values('poker_user_id').distinct().count(), 
            'user' : User.objects.get(id=user),
            'user_poked' : Poke.objects.filter(poked_user_id=user).values('poker_user_id').distinct(),
            'users' : User.objects.exclude(id=user),
        }
    return render(request, 'main/pokes.html', context)

def create(request, user_id):
    user = request.session['id']
    Poke.objects.create(poker_user_id=user, poked_user_id=user_id)
    return redirect('/pokes')


def logout(request):
    del request.session['id']
    return redirect('/main')