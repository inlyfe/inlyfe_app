from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from ticket_services.api.serializers import TripSerializer, SeatSerializer
from ticket_services.models import Trip, Seat, TripGroup

class TripView(ListAPIView):
    serializer_class = TripSerializer
    queryset = Trip.objects.order_by('-created_at')


class TripDetailView(RetrieveAPIView):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()
    lookup_field = 'trip_slug'


class SeatAPIView(ListAPIView):
    serializer_class = SeatSerializer
    queryset = Seat.objects.order_by('-created_at')



class CheckTrip(APIView):
    serializer_class = TripSerializer
    def post(self, request):
        trips = Trip.objects.filter(trip_from=request.data['trip_from'], trip_destination=request.data['trip_destination'], is_arrival=False)
        print(trips)
        response = trips
        return Response({response})
    