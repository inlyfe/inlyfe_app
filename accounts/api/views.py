from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from accounts.api.permissions import IsVendorUser, IsOfficeUser, IsReceptionUser
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from accounts.api.serializers import( 
    UserSerializer, 
    ReceptionSignupSerializer, 
    OfficeSignupSerializer, 
    VendorSignupSerializer
    )


class OfficeSignupView(generics.GenericAPIView):
    serializer_class = OfficeSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'Message': 'User created successfully',
        })


class ReceptionSignupView(generics.GenericAPIView):
    serializer_class = ReceptionSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'Message': 'User created successfully',
        })


class VendorSignupView(generics.GenericAPIView):
    serializer_class = VendorSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'Message': 'User created successfully',
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        picture = user.profile_pic.url
        token, created=Token.objects.get_or_create(user=user)
        # print(token)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'is_vendor': user.is_vendor,
            'profile_pic': picture,
            'is_reception': user.is_reception,
            'is_office': user.is_office,
            'use_visitor': user.visitor_check,
            'use_hotel': user.hotel_service,
            'use_restaurant': user.restaurant_service,
            'bus_ticket_service': user.ticket_service,
            'apartment_service': user.apartment_service,
        })


class Logout(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_100_OK)


class VendorOnlyView(generics.RetrieveAPIView):
    permission_class = [permissions.IsAuthenticated&IsVendorUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



class ReceptionOnlyView(generics.RetrieveAPIView):
    permission_class = [permissions.IsAuthenticated&IsReceptionUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



class OfficeOnlyView(generics.RetrieveAPIView):
    permission_class = [permissions.IsAuthenticated&IsOfficeUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user