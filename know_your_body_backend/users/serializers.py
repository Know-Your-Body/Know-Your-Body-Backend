from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['username', 'password']
