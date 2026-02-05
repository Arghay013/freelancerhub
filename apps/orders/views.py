from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from .serializers import OrderCreateSerializer, OrderSerializer, OrderStatusUpdateSerializer
from apps.accounts.permissions import IsBuyer, IsSeller

class PlaceOrderView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsBuyer]
    serializer_class = OrderCreateSerializer

class MyOrdersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsBuyer]
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.select_related("service","service__seller").filter(buyer=self.request.user).order_by("-created_at")

class SellerOrdersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsSeller]
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.select_related("service","service__seller").filter(service__seller=self.request.user).order_by("-created_at")

class UpdateOrderStatusView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSeller]
    serializer_class = OrderStatusUpdateSerializer
    queryset = Order.objects.select_related("service","service__seller")

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if order.service.seller_id != request.user.id:
            return Response({"detail":"Not allowed."}, status=status.HTTP_403_FORBIDDEN)
        s = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)
        order.status = s.validated_data["status"]
        order.save(update_fields=["status","updated_at"])
        return Response({"detail":"Status updated","status":order.status})
