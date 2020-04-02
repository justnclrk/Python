from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, localtime
import random
def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
        request.session['activity'] = []
    return render(request, 'index.html')

def process(request):
    action = ''
    event = []
    now = strftime("%b %d, %Y %I:%M %p", localtime())

    if request.POST['building'] == 'farm':
        gold = random.randrange(10, 21)
        request.session['gold_count'] += gold
        action = "Earned {} gold from the farm! ({})".format(gold, now)
        event = ['green', action]
        request.session['activity'].insert(0, event)
    
    if request.POST['building'] == 'cave':
        gold = random.randrange(5, 11)
        request.session['gold_count'] += gold
        action = "Earned {} gold from the cave! ({})".format(gold, now)
        event = ['green', action]
        request.session['activity'].insert(0, event)
    
    if request.POST['building'] == 'house':
        gold = random.randrange(2, 6)
        request.session['gold_count'] += gold
        action = "Earned {} gold from the house! ({})".format(gold, now)
        event = ['green', action]
        request.session['activity'].insert(0, event)
    
    if request.POST['building'] == 'casino':
        gold = random.randrange(-50, 51)
        if gold > -1:
            request.session['gold_count'] += gold
            action = "Winner!! You won {} gold at the casino! ({})".format(gold, now)
            event = ['green', action]
            request.session['activity'].insert(0, event)
        else:
            request.session['gold_count'] -= gold
            action = "You lost {} gold from the casino! ({})".format(gold, now)
            event = ['red', action]
            request.session['activity'].insert(0, event)
    return redirect('/')

def reset(request):
    request.session['gold_count'] = 0
    request.session['activity'] = []
    return redirect('/')
