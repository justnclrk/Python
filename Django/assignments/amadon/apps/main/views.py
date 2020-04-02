# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse, redirect
def index(request):
    return render(request, 'index.html')

def buy(request, methods="post"):
    if request.POST["product_id"] == '100':
        price = 19.99
    elif request.POST["product_id"] == '200':
        price = 29.99
    elif request.POST["product_id"] == '300':
        price = 5.99
    elif request.POST["product_id"] == '400':
        price = 49.99
    else:
        price = 0

    count = int(request.POST["quantity"])
 
    request.session["transaction_total"] = count * price
    request.session["count"] += count
    request.session["running_total"] += count * price
    return redirect('/checkout')

def checkout(request):
    if "transaction_total" not in request.session:
        request.session["transaction_total"] = 0
    if "count" not in request.session:
        request.session["count"] = 0
    if "running_total" not in request.session:
        request.session["running_total"] = 0
    context = {
        "transaction_total": request.session["transaction_total"],
        "count": request.session["count"],
        "total": request.session["running_total"]
    }
    return render(request, 'checkout.html', context)

def clear(request):
    del request.session["transaction_total"]
    del request.session["count"]
    del request.session["running_total"]
    return redirect('/checkout')