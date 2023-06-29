from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from accounts.api.permissions import IsVendorUser, IsReceptionUser
from visitors.models import Visitor
from hotels.api.serializers import *
from visitors.api.serializers import VisitorSerializer
from django.views.decorators.csrf import csrf_exempt
from nida import load_user



class VendorVisitorList(ListAPIView):
    # Returns all transactions with filters
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = TransactioFilter
    # permission_classes = (IsAuthenticated,)



class VisitorCreateApi(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VisitorSerializer
    queryset = Visitor.objects.all()


    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Visitor checked in successfull"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)





class RoomView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.order_by('-id')


class RoomDetailView(RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = 'room_slug'


class BookingCreateApiView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Room is successfully booked"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        room = get_object_or_404(Room, pk=request.data['room'])
        if room.is_booked:
            return Response({"response": "Room is already booked"}, status=status.HTTP_200_OK)
        room.is_booked = True
        room.save()
        checked_in_room = CheckIn.objects.create(
            customer=request.user,
            room=room,
            phone_number=request.data['phone_number'],
            email=request.data['email']
        )
        checked_in_room.save()
        return self.create(request, *args, **kwargs)



class CheckoutView(APIView):
    def post(self, request):
        room = get_object_or_404(Room, pk=request.data['pk'])
        checked_in_room = CheckIn.objects.get(room__pk=request.data['pk'])
        print(checked_in_room)
        room.is_booked = False
        room.save()
        checked_in_room.delete()
        return Response({"Checkout Successful"}, status=status.HTTP_200_OK)


class CheckedInView(ListAPIView):
    permission_classes = (IsAdminUser, )
    serializer_class = CheckinSerializer
    queryset = CheckIn.objects.order_by('-id')





@csrf_exempt 
def Kyc(request):
    id_number = request.POST.get('nationalId')
    user_info = load_user(national_id=id_number)
    res = None
    print(user_info)
    if user_info is not None:
        if id_number == user_info.get('Nin'):
            ui = load_user(national_id=id_number)
            # print(ui)
            data = []
            item = {
                'NIN': ui.Nin,
                'FirstName': ui.Firstname,
                'MiddleName': ui.Middlename,
                'LastName': ui.Surname,
                'Sex': ui.Sex,
            }
            data.append(item)
            res = data
            print(res)
    else:
        res = 'No data match!'
    return JsonResponse({'data': res})


