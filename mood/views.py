# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

def moodhistory(self):
    """XXX: this will eventually need some kind of date selection"""
    data = {
     'snapshots' : Snapshot.objects.all(),
     'aspects'   : Aspect.objects.all(),
     }
    return render_to_response('mood.moodhistory.html', data)
