from django.db import models
from geoposition import Geoposition
from geoposition.fields import GeopositionField
# Create your models here.

class Event(models.Model):
    def __str__(self):
        return self.event_name
    category=(('A','Art'),('F','Food'),('M','Music'),('S','Shopping'),('T','Theatre'))
    paid=(('P','Paid'),('F','Free'))
    event_name=models.CharField(max_length=200)
    event_date=models.DateTimeField('event date')
    event_category=models.CharField(max_length=20,choices=category,default='Null')
    event_website=models.CharField(max_length=200,blank=True)
    event_metro=models.CharField(max_length=200,blank=True)
    event_venue=models.CharField(max_length=200,blank=True)
    event_paid=models.CharField(max_length=20,choices=paid,default="Null")
    
class Location(models.Model):
    venue=models.ForeignKey(Event,on_delete=models.CASCADE)
    event_position=GeopositionField()
    
class PaidEvent(models.Model):
    def __str__(self):
        return self.event_bms
    def limit():
        return({'event_paid':'P'})
    bms = models.ForeignKey(Event,on_delete=models.CASCADE,limit_choices_to= limit())
    event_bms=models.CharField(max_length=200,default=" ",blank=True)




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
