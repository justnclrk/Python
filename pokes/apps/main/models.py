# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = "Name is required, must be at least 3 characters!"
        if len(postData['alias']) < 3:
            errors['alias'] = "Alias is required, must be at least 3 characters!"
        elif len(User.objects.filter(alias=postData["alias"])):
            errors['alias'] = "Alias already in use, try again"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Must be a valid email!"
        elif len(User.objects.filter(email=postData["email"])):
            errors['email'] = "Email already in use, try again"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        if  postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords must match!"
        if len(postData['dob']) == 0:
            errors['dob'] = "Please enter a Date of Birth!"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
    def __str__(self):
        return self.name

class Poke(models.Model):
    poker_user = models.ForeignKey(User, related_name="poker")
    poked_user = models.ForeignKey(User, related_name="poked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()