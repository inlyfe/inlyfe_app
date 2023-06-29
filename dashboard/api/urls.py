from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from dashboard.api.views import *
from visitors_data_strg.api.views import VisitorRegisterApi

# app_name = 'visitor_api'

urlpatterns = [
    path('visitors/', VendorVisitorList.as_view(), name='visitors'),
    path('visitor/create/', VisitorCreateApi.as_view(), name='visitor_create'),
    # visitor registration url
    path('visitor/register/', csrf_exempt(VisitorRegisterApi.as_view()), name='visitor_register'),

    path('get_room_list/', RoomView.as_view(), name="room_list"),
    path('get_a_room_detail/<str:room_slug>/', RoomDetailView.as_view(), name="single_room"),
    path('book/', BookingCreateApiView.as_view(), name='book_room'),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('get_current_checked_in_rooms/', CheckedInView.as_view(), name="checked_in_rooms"),

    path('kyc/', Kyc, name="kyc"),
]
