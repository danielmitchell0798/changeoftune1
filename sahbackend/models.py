from django.db import models
from django.utils import timezone

# Create your models here.
class Institution(models.Model):
    institution_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.institution_name)

class Location(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    location_number = models.IntegerField(blank=True, null=False)
    institution_num = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='locationinst')
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)

class Volunteer(models.Model):
    institution_num = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='volunteerinst')
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.first_name)

class Flier(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='volunteerFlier')
    start_time = models.TimeField(default=timezone.now, blank=True, null=True)
    end_time = models.TimeField(default=timezone.now, blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.volunteer)

class Reservation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locationReservation')
    start_time = models.TimeField(default=timezone.now, blank=True, null=True)
    end_time = models.TimeField(default=timezone.now, blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.location)

class Event(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locationEvent')
    flier = models.ForeignKey(Flier, on_delete=models.CASCADE, related_name='flierEvent')
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reservationEvent')
    name = models.CharField(max_length=50, blank=False)
    start_time = models.TimeField(default=timezone.now, blank=False, null=True)
    end_time = models.TimeField(default=timezone.now, blank=False, null=True)
    date = models.DateField(default=timezone.now, blank=False, null=True)
    description = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.location)

class BlogPage(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='blogpage')
    title =  models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.volunteer)

class FoodPickUp(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='foodrequest')
    request_title = models.CharField(max_length=50, blank=True)
    request_time = models.TimeField(default=timezone.now, blank=False, null=True)
    request_date = models.DateField(default=timezone.now, blank=False, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.location)