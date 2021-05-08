from django.contrib import admin
from .models import BlogPage, FoodPickUp, Institution, Volunteer, Flier, Event, Location, Reservation

class InstitutionList(admin.ModelAdmin):
    list_display = ('institution_name', 'address', 'city', 'state', 'zipcode', 'phone')
    list_filter = ('institution_name', 'phone')
    search_fields = ['institution_name']
    ordering = ['institution_name']

class VolunteerList(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone')
    list_filter = ['institution_num']
    search_fields = ('first_name', 'last_name', 'institution_num')
    ordering = ['first_name']

class LocationList(admin.ModelAdmin):
    list_display = ( 'name', 'location_number')
    list_filter = ['location_number']
    search_fields = ['name']
    ordering = ['location_number']

class FlierList(admin.ModelAdmin):
    list_display = ('volunteer', 'start_time', 'end_time', 'date')
    list_filter = ('volunteer', 'date')
    search_fields = ['volunteer']
    ordering = ['date']

class EventList(admin.ModelAdmin):
    list_display = ('name', 'location', 'flier', 'reservation', 'start_time', 'end_time', 'date')
    list_filter = ('name', 'location', 'date')
    search_fields = ('name', 'location')
    ordering = ['location']

class ReservationList(admin.ModelAdmin):
    list_display = ('location', 'start_time', 'end_time', 'date')
    list_filter = ('location', 'date')
    search_fields = ['location']
    ordering = ['date']

class BlogPageList(admin.ModelAdmin):
    list_display = ('volunteer', 'title')
    list_filter = ['volunteer']
    search_fields = ('volunteer', 'title')
    ordering = ['volunteer']

class FoodPickUpList(admin.ModelAdmin):
    list_display = ('request_title', 'location', 'request_time', 'request_date')
    list_filter = ('location', 'request_date')
    search_fields = ('location', 'request_date')
    ordering = ['location']

admin.site.register(BlogPage, BlogPageList)
admin.site.register(FoodPickUp, FoodPickUpList)
admin.site.register(Institution, InstitutionList)
admin.site.register(Location, LocationList)
admin.site.register(Event, EventList)
admin.site.register(Reservation, ReservationList)
admin.site.register(Flier, FlierList)
admin.site.register(Volunteer, VolunteerList)