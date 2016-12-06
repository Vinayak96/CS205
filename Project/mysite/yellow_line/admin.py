from django.contrib import admin

# Register your models here.
from .models import Event,PaidEvent,Location

class LocationInline(admin.StackedInline):
    model= Location
    extra=1
class PaidEventInline(admin.StackedInline):
    model=PaidEvent
    extra=1

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['event_name']}),
        ('Date information', {'fields': ['event_date']}),
        ('Venue',{'fields':['event_venue']}),
        ('Category',{'fields':['event_category']}),
        ('Webpage',{'fields':['event_website']}),
        ('Paid Event',{'fields':['event_paid']})
        
    ]
    inlines =[LocationInline,PaidEventInline]
    
    list_filter = ['event_name', 'event_date','event_category','event_paid','event_venue']



admin.site.register(Event,EventAdmin)
