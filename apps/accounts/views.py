from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import EmailVerificationToken
from .serializers import RegisterSerializer, VerifyEmailSerializer, MeSerializer

class VerifiedTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if not getattr(self.user, "is_verified", False):
            raise PermissionError("Email not verified.")
        return data

class TokenView(TokenObtainPairView):
    serializer_class = VerifiedTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token_obj = EmailVerificationToken.objects.get(user=user)
        verify_url = f"{settings.SITE_URL}/api/auth/verify-email/"
        msg = f"Verify your email. POST {verify_url} with token: {token_obj.token}"
        send_mail("Verify your email", msg, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=True)

class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        s = VerifyEmailSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        token = s.validated_data["token"]
        try:
            t = EmailVerificationToken.objects.select_related("user").get(token=token)
        except EmailVerificationToken.DoesNotExist:
            return Response({"detail":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        t.user.is_verified = True
        t.user.save(update_fields=["is_verified"])
        t.delete()
        return Response({"detail":"Email verified. You can now log in."})

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh = request.data.get("refresh")
        if not refresh:
            return Response({"detail":"refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            RefreshToken(refresh).blacklist()
        except Exception:
            return Response({"detail":"Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail":"Logged out"})

class MeView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MeSerializer
    def get_object(self):
        return self.request.user
