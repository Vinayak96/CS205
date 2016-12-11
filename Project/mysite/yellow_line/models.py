from django.db import models
from geoposition import Geoposition
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.
#Class to store all event information
class Event(models.Model):                                     
    """
    Creates a table of all event fields in the database
    """
    def __str__(self):
        return self.event_name

#All possible Event categories
    category=(('Art','Art'),('Food','Food'),('Music','Music'),('Shopping','Shopping'),('Theatre','Theatre'))       
    paid=(('Paid','Paid'),('Free','Free'))
#Name of the event
    event_name=models.CharField(max_length=200,help_text="Please enter name of the event and make sure it begins with a capital letter")                                     
#Date of the event
    event_date=models.DateTimeField('event date',help_text="Please choose the date of the event.")
#Category of the event
    event_category=models.CharField(max_length=20,choices=category,default='Null', help_text="Please choose what category the event falls under.")
#Website of the event
    event_website=models.CharField(max_length=200,blank=True,help_text="Please enter a link to the event website or Facebook page." )
#Nearest Metro Station to the Event
    event_metro=models.CharField(max_length=200,blank=True,help_text="Please enter the name of the nearest metro station")
 #Venue of the event
    event_venue=models.CharField(max_length=200,blank=True,help_text="Please enter the name of the venue of the event.")
#Stores whether event is paid or unpaid
    event_paid=models.CharField(max_length=20,choices=paid,default="Null",help_text="Please choose if the event is paid or free.")
#Image for the event
    event_image=models.ImageField(upload_to='/static/yellow_line/event_images', blank=True, help_text="Please upload an image for the event.")          
    class Meta:
        app_label = "yellow_line"

    
#Gets the location of the venue of the event
class Location(models.Model):                                 
    """
    Admin stores the location of the event using the geoposition app
    Parameters:
    'event_position': A field which stores latitude and longitude of event
    """
    venue=models.ForeignKey(Event,on_delete=models.CASCADE)
    event_position=GeopositionField()

#Class to get the ticketbooking link for a paid event    
class PaidEvent(models.Model):                               
    def __str__(self):
        return self.event_bms
    def limit():
        return({'event_paid':'Paid'})
    bms = models.ForeignKey(Event,on_delete=models.CASCADE,limit_choices_to= limit())
#Link to ticketbooking page
    event_bms=models.CharField(max_length=200,default=" ",blank=False)                #Link to ticketbooking page

class UserProfile(models.Model):
    category=(('Art','Art'),('Food','Food'),('Music','Music'),('Shopping','Shopping'),('Theatre','Theatre'))

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    

    # The additional attributes we wish to include.
    interest = MultiSelectField(max_length=20,choices=category,default='Null', help_text="Please choose what categories you like")
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.first_name




##class EventManager(models.Manager):
##    def get_querysetName(self):
##        return Event.objects.order_by('event_name')
##    def get_querysetDate(self):
##        return Event.objects.order_by('event_date')
##    def get_querysetCategory(self):
##        return Event.objects.order_by('event_category')
##    def get_querysetVenue(self):
##        return Event.objects.order_by('event_venue')
##    def searchName(self,a):
##        return Event.objects.filter(event_name = a)
##
