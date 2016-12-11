from django.shortcuts import render, render_to_response
from yellow_line.models import *
from django.template import loader, RequestContext
# Create your views here.
from django.http import HttpResponse
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
    template=loader.get_template('yellow_line/index.html')
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
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)        
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # # Now sort out the UserProfile instance.
            # # Since we need to set the user attribute ourselves, we set commit=False.
            # # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'interest' in request.FILES:
                profile.interest = request.FILES['interest']

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
