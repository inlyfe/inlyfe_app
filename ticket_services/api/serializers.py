from ticket_services.models import Seat, Trip, TripGroup, Ticket, CheckIn, Passenger
from rest_framework import serializers


class TripSerializer(serializers.ModelSerializer):
    group_name =serializers.CharField(source='group.group_name')

    class Meta:
        model = Trip
        fields = '__all__'


    def create(self, validated_data):
        return super().create(self.group_name)



class SeatSerializer(serializers.ModelSerializer):
    group_name =serializers.CharField(source='group.group_name')

    class Meta:
        model = Seat 
        fields = '__all__'


    def create(self, validated_data):
        return super().create(self.group_name)


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger 
        fields = '__all__'



class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket 
        fields = '__all__'






    

