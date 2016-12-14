from django.shortcuts import render, render_to_response
from yellow_line.models import *
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .forms import *
from django.views.decorators.csrf import csrf_exempt

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
    template=loader.get_template('yellow_line/search.html')
    context ={
        'event_list':event_list,
        }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def signup(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)        
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # hashing the password with the set_password method.
            # Updating the user object after hashing
            user.set_password(user.password)
            user.save()

            # # Now sort out the UserProfile instance.
            # # Since we need to set the user attribute ourselves, we set commit=False.
            # # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

##            if 'interest' in request.FILES:
##                profile.interest = request.FILES['interest']

            # # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'yellow_line/signup.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},context)

@csrf_exempt
def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # # Is the account active? It could have been disabled.
            # if user.is_active:
            #     # If the account is valid and active, we can log the user in.
            #     # We'll send the user back to the homepage.
            login(request, user)
            return HttpResponseRedirect('/yellow_line/')
            # else:
            #     # An inactive account was used - no logging in!
            #     return HttpResponse("Your Yellow Line account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('yellow_line/login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
#@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/yellow_line/login/')

#customized display when user logs in
def user_view(request):
    current_user=request.user
    result_list=[]
    categories = [('Art',current_user.art),('Theatre',current_user.theatre),('Food',current_user.food),('Music',current_user.music),('Shopping',current_user.shopping)]
    for i in range(5):
        result_list.append(query_gen(categories[i]))
    template=loader.get_template('yellow_line/index.html')
    context ={
        'result_list':result_list,
        }
    return HttpResponse(template.render(context, request))    

def query_gen(y,x):
    if x is True :
        return Event.objects.filter(event_category=y)
