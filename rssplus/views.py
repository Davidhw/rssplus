from django.shortcuts import render,redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from forms import URLForm

import json
import urllib2
import sys
import os
from subscribe.models import Subscription
def home(request):
    form = URLForm()
    return render_to_response('home-view.html',{"subscriptionsString":Subscription.getStringOfAll(),"urlForm":form},context_instance=RequestContext(request))















