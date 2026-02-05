from rest_framework import serializers
from .models import Order
from apps.services.models import Service

class OrderCreateSerializer(serializers.ModelSerializer):
    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ("id","service_id","note","status","created_at")
        read_only_fields = ("id","status","created_at")

    def validate_service_id(self, value):
        if not Service.objects.filter(id=value, is_active=True).exists():
            raise serializers.ValidationError("Service not found or inactive.")
        return value

    def create(self, validated_data):
        service = Service.objects.get(id=validated_data.pop("service_id"))
        return Order.objects.create(buyer=self.context["request"].user, service=service, **validated_data)

class OrderSerializer(serializers.ModelSerializer):
    service_title = serializers.CharField(source="service.title", read_only=True)
    service_price = serializers.DecimalField(source="service.price", max_digits=10, decimal_places=2, read_only=True)
    seller_username = serializers.CharField(source="service.seller.username", read_only=True)

    class Meta:
        model = Order
        fields = ("id","service","service_title","service_price","seller_username","status","note","created_at","updated_at")
        read_only_fields = fields

class OrderStatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Order.Status.choices)
