
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import (
    TripView, 
    TripDetailView, 
    SeatAPIView,
    CheckTrip,
    # BookingCreateApiView, 
    # CheckoutView, 
    # CheckedInView
    )

app_name = 'hotel_app'

urlpatterns = [
    path('get_trip_list/', TripView.as_view(), name="room_list"),
    path('get_a_trip_detail/<str:trip_slug>/', TripDetailView.as_view(), name="single_trip"),
    path('get_seat_list/', SeatAPIView.as_view(), name='trip_list'),
    path('fetch_trip/', csrf_exempt(CheckTrip.as_view()), name='fetch_trip'),
    # path('checkout/', CheckoutView.as_view(), name="checkout"),
    # path('get_current_checked_in_rooms/', CheckedInView.as_view(), name="checked_in_rooms"),
]
