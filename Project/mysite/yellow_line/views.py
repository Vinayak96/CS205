from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse(Event.objects.all())

def displayname(request):
    return HttpResponse(Event.objects.order_by('event_name'))

def displaydate(request):
    return HttpResponse(Event.objects.order_by('event_date'))

def displaycategory(request):
    return HttpResponse(Event.objects.order_by('event_category'))

def displayvenue(request):
    return HttpResponse(Event.objects.order_by('event_venue'))

def searchcategory(request,a):
    return HttpResponse(Event.objects.filter(event_category = a[0]))

