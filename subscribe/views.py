from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
import json
import urllib2
import sys
import os
from models import Subscription
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# Create your views here.

def console_debug(f):
    def x(*args, **kw):
        try:
            ret = f(*args, **kw)
        except Exception, e:
            print >> sys.stderr, "ERROR:", str(e)
            exc_type, exc_value, tb = sys.exc_info()
            message = "Type: %s\nValue: %s\nTraceback:\n\n%s" % (exc_type, exc_value, "\n".join(traceback.format_tb(tb)))
            print >> sys.stderr, message
            raise
        else:
            return ret
        return x

def save(request):
#    body = simplejson.loads(request.body)
    body = json.loads(request.body)

    with open("RSSlog.txt",'w')as log:
        log.write(str(body.items()))
        log.write("in save")

    url = body['url']
    xpath = body['xpath']
    subscription = Subscription()
    subscription.url = url
    subscription.xpath = xpath
    subscription.save()
    return HttpResponseRedirect('/subscribe/')

def load_external_page(request,url):
    print >>sys.stderr, url
    html = urllib2.urlopen(url).read()
    split = html.split("</head>")
    if len(split)==2:
        html1 = html[0:len(split[0])+len("</head>")]
        html2 = split[1]
    else:
        html1 = html
        html2 = ""
#    html1 = html.split("/head>")[0]
#    html2 = html.split("/head>")[1]
#    html = "<h1 hi />"
#    return render(request,'subscribe-view.html')
#    return render(request,'subscribe-view.html',{'html':html,'url':url},dirs = (PROJECT_ROOT+"/subscribe/templates/subscribe/",PROJECT_ROOT+"subscribe/templates/"))
#    with open("RSSlog.txt",'w') as log:
#        log.write("writing html of"+url)
#        log.write(url)
    return render(request,'subscribe-view.html',{'html1':html1,'html2':html2,'url':url})















