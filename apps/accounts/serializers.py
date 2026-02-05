from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import EmailVerificationToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("username","email","password","role")

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            role=validated_data["role"],
            is_verified=False,
            is_active=True,
        )
        user.set_password(validated_data["password"])
        user.save()
        EmailVerificationToken.objects.update_or_create(user=user, defaults={})
        return user

class VerifyEmailSerializer(serializers.Serializer):
    token = serializers.UUIDField()

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","role","is_verified")
