from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from know_your_body_backend.users import models, serializers


class SignUpUserView(APIView):

    def post(self, request, format='json'):
        serializer = serializers.UserSignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                user_data = {'auth_token': token.key}
                return Response(user_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserBMIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format='json'):
        bmi_data = models.UserBMI.objects.filter(user=request.user.id)
        serializer = serializers.UserBMISerializer(bmi_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        request.data['user'] = request.user.id
        serializer = serializers.UserBMISerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response('', status=status.HTTP_400_BAD_REQUEST)


class UserHemoglobinView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format='json'):
        hemoglobin_data = models.UserHemoglobin.objects.filter(user=request.user.id)
        serializer = serializers.UserHemoglobinSerializer(hemoglobin_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        request.data['user'] = request.user.id
        serializer = serializers.UserHemoglobinSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response('', status=status.HTTP_400_BAD_REQUEST)


class UserBloodSugarView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format='json'):
        bmi_data = models.UserBloodSugar.objects.filter(user=request.user.id)
        serializer = serializers.UserBloodSugarSerializer(bmi_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        request.data['user'] = request.user.id
        serializer = serializers.UserBloodSugarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response('', status=status.HTTP_400_BAD_REQUEST)
