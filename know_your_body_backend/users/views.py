from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from know_your_body_backend.users import serializers


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
