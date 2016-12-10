from django.shortcuts import render
from yellow_line.models import Event,PaidEvent,Location
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
##from .forms import searchform

def index(request):
    """
    Creates a list of all events in the database and returns it,
    related to :model: 'yellow_line.Event'
    """
    event_list = Event.objects.all()
    template=loader.get_template('yellow_line/index.html')
    context ={
        'event_list':event_list,
        }
    return HttpResponse(template.render(context,request))

def displayname(request):
    """
    Creates a list of all events, ordered by name,related to

    :model:'yellow_line.Event'

    :template:'yellow_line/index.html'

    """
    event_list = Event.objects.order_by('event_name')
    template=loader.get_template('yellow_line/index.html')
    context ={
        'event_list':event_list,
        }
    return HttpResponse(template.render(context,request))

def displaydate(request):
    """
    Creates a list of all events, ordered by date,
    related to :model: 'yellow_line.Event'
    """
    event_list = Event.objects.order_by('event_date')
    template=loader.get_template('yellow_line/index.html')
    context ={
        'event_list':event_list,
        }
    return HttpResponse(template.render(context,request))

def displaycategory(request):
    """
    Creates a list of all events, ordered by category,
    related to :model: 'yellow_line.Event'
    """
    event_list = Event.objects.order_by('event_category')
    template=loader.get_template('yellow_line/index.html')
    context ={
        'event_list':event_list,
        }
    return HttpResponse(template.render(context,request))
    

def displayvenue(request):
    """ Creates a list of all events, ordered by venue """
    event_list = Event.objects.order_by('event_venue')
    template=loader.get_template('yellow_line/index.html')
    context ={
        'event_list':event_list,
        }
    return HttpResponse(template.render(context,request))


def searchcategory(request, a):
    """
    Searches for input value across all fields in the table,
    related to :model: 'yellow_line.Event'
    """
    event_list = Event.objects.filter(Q(event_category__contains = a) | Q(event_name__contains= a) | Q(event_venue__contains = a))
    template=loader.get_template('yellow_line/index.html')
    context ={
        'event_list':event_list,
        }
    return HttpResponse(template.render(context, request))

##def getsearch(request,a):
##    if request.method=='POST':
##        form = searchform(request.POST)
##        if form.is_valid():
##            event_list = Event.objects.filter(Q(event_category__contains = a) | Q(event_name__contains= a) | Q(event_venue__contains = a))
##            template=loader.get_template('yellow_line/index.html')
##            context ={
##                'event_list':event_list,
##            }
##        return HttpResponse(template.render(context, request))
##    else:
##        form = searchform()

##from yellow_line.forms import *
##from django.contrib.auth.decorators import login_required
##from django.contrib.auth import logout
##from django.views.decorators.csrf import csrf_protect
##from django.shortcuts import render_to_response
##from django.http import HttpResponseRedirect
##from django.template import RequestContext
## 
##@csrf_protect
##def register(request):
##    if request.method == 'POST':
##        form = RegistrationForm(request.POST)
##        if form.is_valid():
##            user = User.objects.create_user(
##            username=form.cleaned_data['username'],
##            password=form.cleaned_data['password1'],
##            email=form.cleaned_data['email']
##            )
##            return HttpResponseRedirect('/register/success/')
##    else:
##        form = RegistrationForm()
##    variables = RequestContext(request, {
##    'form': form
##    })
## 
##    return render_to_response(
##    'registration/register.html',
##    variables,
##    )
## 
##def register_success(request):
##    return render_to_response(
##    'registration/success.html',
##    )
## 
##def logout_page(request):
##    logout(request)
##    return HttpResponseRedirect('/')
## 
##@login_required
##def home(request):
##    return render_to_response(
##    'home.html',
##    { 'user': request.user }
##    )
