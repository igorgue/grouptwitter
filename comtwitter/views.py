# Django imports 
from django.http import HttpResponse 
from django.conf import settings
from django.utils import simplejson
from django.shortcuts import render_to_response

#return HttpResponse(cjson.encode(latest_info), mimetype="application/json")

# Twitter imports
from pytwitter import pytwitter

# Local exceptions
class TwitterError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Index page
def index(request):
    """
    homepage
    
    request -- httprequest object
    """
    updates = simplejson.loads(tw_timeline())
    return render_to_response('index.html', {'updates': updates})

# Function to post in twitter and return an obj using ajax
def update(request, status):
    """
    Update status in twitter
    
    request -- httprequest obj
    """
    return HttpResponse(tw_post(status), mimetype="application/json")

# Function to show a twitter status
def show(request, status):
    """
    Update status in twitter
    
    request -- httprequest obj
    status -- requested status
    """
    return HttpResponse(tw_show(status), mimetype="application/json")

# Function to post an update in twitter
def tw_post(update, format='json'):
    """
    Post a twitter update
    
    update -- update content
    format -- format of the resulting request
    """
    if format != 'json' and format != 'xml':
        raise TwitterError('incorrect twitter API format output')
    if len(update) > 140:
        raise TwitterError('The tweet is to big... we only accept 140 chars per tweet :)')
    
    client = pytwitter(username=settings.TWITTER_ACCOUNT, password=settings.TWITTER_PASSWORD, format=format)
    return client.statuses_update(status=update)

# Function to get the user timeline
def tw_timeline(format='json'):
    """
    Get the user timeline, documentation here: http://apiwiki.twitter.com/REST+API+Documentation#usertimeline
    
    format -- format of the resulting request
    """
    if format != 'json' and format != 'xml':
        raise TwitterError('incorrect twitter API format output')

    client = pytwitter(username=settings.TWITTER_ACCOUNT, password=settings.TWITTER_PASSWORD, format=format)
    return client.statuses_user_timeline(id=settings.TWITTER_ACCOUNT)

# Function to show a tweet
def tw_show(id, format='json'):
    """
    Show a status
    
    id -- the tweet id to show
    format -- format of the resulting request
    """
    client = pytwitter(username=settings.TWITTER_ACCOUNT, password=settings.TWITTER_PASSWORD, format=format)
    return client.statuses_show(id=id)
