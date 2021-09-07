from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationView(APIView):
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        queryset = User.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

class ApiTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data ="hello %s, your are logged in succesfully"%(request.user.username)
        return Response(data)


