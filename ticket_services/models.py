from django.db import models
from accounts.models import User, Vendor, Reception


def seat_images_upload_path(instance, file_name):
    return f"{instance.seat_slug}/seat_cover/{file_name}"


def seat_display_images_upload_path(instance, file_name):
    return f"{instance.seat.seat_slug}/seat_display/{file_name}"


class Seat(models.Model):
    seat_number = models.CharField(max_length=50)
    fare = models.CharField(max_length=50)
    group = models.ForeignKey("TripGroup", on_delete=models.CASCADE, related_name="seat_group")
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name="seat_trip")
    is_arrival = models.BooleanField(default=False)
    seat_slug = models.SlugField()
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, null=True, auto_now_add=True)
    belongs_to = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
  

    def __str__(self):
        return self.seat_number
    
    


class Trip(models.Model):
    trip_from = models.CharField(max_length=250)
    trip_destination = models.CharField(max_length=250)
    group = models.ForeignKey("TripGroup", on_delete=models.CASCADE)
    trip_number = models.CharField(max_length=50)
    trip_slug = models.SlugField(null=True)
    is_arrival = models.BooleanField(default=False)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=False, null=True, auto_now_add=True)
    belongs_to = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.trip_from


class TripGroup(models.Model):
    group_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, null=True, auto_now_add=True)

    def __str__(self):
        return self.group_name


class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)
    attachment = models.ImageField(upload_to=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=False, null=True, auto_now_add=True)


    def __str__(self):
        return self.first_name


class Ticket(models.Model):
    passenger = models.ForeignKey("Passenger", on_delete=models.CASCADE, related_name="passenger_ticket")
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name="ticket_trip")
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE, related_name="ticket_seat")
    ticket_number = models.CharField(max_length=50)
    booking_date = models.DateTimeField(auto_now_add=True)
    checking_date = models.DateTimeField(blank=True, null=True)
    checkout_date = models.DateTimeField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    belongs_to = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)
    created_by= models.ForeignKey(Reception, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.passenger.first_name


class CheckIn(models.Model):
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE, related_name="passenger_checkin")
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE, related_name="checkin_seat")
    phone_number = models.CharField(max_length=14, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.seat.seat_slug


class CheckOut(models.Model):
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE, related_name="passenger_checkout")
    check_out_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.passenger.first_name



class Payment(models.Model):
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=False, null=True, auto_now_add=True)

    def __str__(self):
        return self.passenger



class SeatDisplayImages(models.Model):
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE, related_name="seat_images_display")
    display_images = models.ImageField(upload_to=seat_display_images_upload_path)

    def __str__(self):
        return self.seat.seat_slug
