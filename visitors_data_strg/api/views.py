from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from visitors_data_strg.api.serializers import CitizenSerializer
from visitors_data_strg.models import Citizen


class VisitorRegisterApi(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CitizenSerializer
    queryset = Citizen.objects.all()


    def create(self, request, *args, **kwargs):
        response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response['data'] = serializer.data
        response['response'] = "Visitor Registered Successfull"
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

