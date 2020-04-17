# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First Name is required, must be at least 2 characters!"
        elif not postData['fname'].isalpha():
            errors['fname'] = "First name must contain only letters!"
        if len(postData['lname']) < 2:
            errors['lname'] = "Last Name is required, must be at least 2 characters!"
        elif not postData['lname'].isalpha():
            errors['lname'] = "Last name must contain only letters!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Must be a valid email!"
        elif len(User.objects.filter(email=postData["email"])):
            errors['email'] = "Email already in use, try again"
        if len(postData['password']) < 8:
            errors['password'] = "Password is required, must be at least 8 characters!"
        if  postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords must match!"
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, related_name="reviews")
    rating = models.SmallIntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()