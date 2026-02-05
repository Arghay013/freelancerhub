from rest_framework import serializers
from .models import Review
from apps.orders.models import Order

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id","service","rating","comment","created_at")
        read_only_fields = ("id","created_at")

    def validate_rating(self, v):
        if v < 1 or v > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return v

    def validate(self, attrs):
        user = self.context["request"].user
        service = attrs["service"]
        if not Order.objects.filter(buyer=user, service=service, status=Order.Status.COMPLETED).exists():
            raise serializers.ValidationError("You can review only after the order is completed.")
        return attrs

    def create(self, validated_data):
        return Review.objects.create(buyer=self.context["request"].user, **validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    buyer_username = serializers.CharField(source="buyer.username", read_only=True)
    class Meta:
        model = Review
        fields = ("id","buyer_username","rating","comment","created_at")
