from django.db import models
from geoposition import Geoposition
from geoposition.fields import GeopositionField
# Create your models here.

class Event(models.Model):
    def __str__(self):
        return self.event_name
    category=(('Art','Art'),('Food','Food'),('Music','Music'),('Shopping','Shopping'),('Theatre','Theatre'))
    paid=(('Paid','Paid'),('Free','Free'))
    event_name=models.CharField(max_length=200)
    event_date=models.DateTimeField('event date')
    event_category=models.CharField(max_length=20,choices=category,default='Null')
    event_website=models.CharField(max_length=200,blank=True)
    event_metro=models.CharField(max_length=200,blank=True)
    event_venue=models.CharField(max_length=200,blank=True).
    event_paid=models.CharField(max_length=20,choices=paid,default="Null")
    
class Location(models.Model):
    """
    Admin stores the location of the event using the geoposition app
    Parameters:
    'event_position': A field which stores latitude and longitude of event
    """
    venue=models.ForeignKey(Event,on_delete=models.CASCADE)
    event_position=GeopositionField()
    
class PaidEvent(models.Model):
    def __str__(self):
        return self.event_bms
    def limit():
        return({'event_paid':'Paid'})
    bms = models.ForeignKey(Event,on_delete=models.CASCADE,limit_choices_to= limit())
    event_bms=models.CharField(max_length=200,default=" ",blank=False)




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
