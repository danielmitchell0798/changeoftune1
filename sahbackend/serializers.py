from rest_framework import serializers
from .models import BlogPage, FoodPickUp, Institution, Volunteer, Event, Location, Reservation, Flier

class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
            model = Institution
            fields = ('pk', 'institution_name', 'address', 'city', 'state', 'zipcode', 'phone')

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
            model = Volunteer
            fields = ('pk', 'institution_num', 'first_name', 'last_name', 'email', 'phone')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
            model = Event
            fields = ('pk', 'location', 'flier', 'reservation', 'name', 'start_time', 'end_time', 'date', 'description')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
            model = Location
            fields = ('pk', 'location_number', 'institution_num', 'name')

class FlierSerializer(serializers.ModelSerializer):
    class Meta:
            model = Flier
            fields = ('pk', 'volunteer', 'start_time', 'end_time', 'date', 'description')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
            model = Reservation
            fields = ('pk', 'location', 'start_time', 'end_time', 'date', 'description')

class BlogPageSerializer(serializers.ModelSerializer):

    class Meta:
            model = BlogPage
            fields = ('pk', 'volunteer', 'title', 'description')

class FoodRequestSerializer(serializers.ModelSerializer):

    class Meta:
            model = FoodPickUp
            fields = ('pk', 'location', 'request_time', 'request_date')

