from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Review
from .serializers import ReviewCreateSerializer, ReviewSerializer
from apps.accounts.permissions import IsBuyer

class CreateReviewView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsBuyer]
    serializer_class = ReviewCreateSerializer

class ServiceReviewsView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.select_related("buyer").filter(service_id=self.kwargs["service_id"]).order_by("-created_at")
