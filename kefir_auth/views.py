from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kefir_auth.serializers import LoginSerializer
from users.serializers import KefirUserSerializer

from loguru import logger


class LoginView(APIView):
    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        logger.info(f"serializer: {login_serializer}")
        if login_serializer.is_valid():
            user_instance = authenticate(
                username=login_serializer.data.get("username"),
                password=login_serializer.data.get("password")
            )
            if user_instance:
                login(request, user_instance)
                user_serializer = KefirUserSerializer(user_instance)
                response = Response(data=user_serializer.data)
                response.set_cookie(key="my_cookie", value="testing_cookie", secure=True, httponly=True, samesite='Lax')
                return response
            return Response(data="Invalid credentials provided", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response(data="Invalid input", status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        response = Response(data="User logout", status=status.HTTP_200_OK)
        response.delete_cookie(key="my_cookie")
        return response


