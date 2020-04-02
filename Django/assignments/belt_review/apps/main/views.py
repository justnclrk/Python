# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from .models import User, Book, Review
import bcrypt
import re

from django.shortcuts import render, HttpResponse, redirect
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
        return redirect('/books')

def login(request):
    try:
        user = User.objects.get(email=request.POST["email"])
    except:
        messages.error(request, "Login Failed, invalid email")
        return redirect('/')

    if bcrypt.checkpw(request.POST["password"].encode(), user.password.encode()):
        request.session["id"] = user.id
        return redirect('/books')
    else:
        messages.error(request, "Login Failed, invalid password")
        return redirect('/')

def log_out(request):
    users = User.objects.all()
    for user in users:
        user.delete()
    return redirect('/')

def books(request):
    user = User.objects.get(id=request.session["id"])
    context = {
        'name': user.fname,
        'books': Book.objects.all()
    }
    return render(request, 'main/homepage.html', context)

def bookadd(request):
    return render(request, 'main/add_book.html')

def create_book(request):
    title = request.POST['title']
    author = request.POST['author']
    Book.objects.create(title=title, author=author) 
    content = request.POST['content']
    book_id = request.session['id']
    Review.objects.create(content=content, user_id=user)
    return redirect('/books')

def review_create(request):
    if 'id' not in request.session['id']:
        return redirect('/')
    return render(request, 'main/book_reviews.html')

def delete(request, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('/books')

def users(request,user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request,'/user_page.html', context)