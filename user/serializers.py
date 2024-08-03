from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Employee


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = Employee.objects.create_user(
            username=validated_data["email"], email=validated_data["email"], password=validated_data["password"]
        )
        return user


class EmailTokenObtainSerializer(TokenObtainSerializer):
    username_field = Employee.EMAIL_FIELD


class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         return token

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         user = authenticate(request=self.context.get('request'), email=email, password=password)
#         if user is None:
#             raise serializers.ValidationError('Invalid email or password')

#         return {
#             'refresh': str(self.get_token(user)),
#             'access': str(self.get_token(user).access_token),
#         }
