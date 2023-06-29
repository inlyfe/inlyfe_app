from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Seat)
admin.site.register(TripGroup)
admin.site.register(Trip)
admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(SeatDisplayImages)
admin.site.register(Payment)
