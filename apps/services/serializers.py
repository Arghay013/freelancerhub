from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    seller_username = serializers.CharField(source="seller.username", read_only=True)

    class Meta:
        model = Service
        fields = ("id","title","description","price","category","delivery_time_days","requirements","is_active","seller","seller_username","created_at")
        read_only_fields = ("id","seller","seller_username","created_at")

    def create(self, validated_data):
        validated_data["seller"] = self.context["request"].user
        return super().create(validated_data)
