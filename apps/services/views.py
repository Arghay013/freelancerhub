from rest_framework import viewsets, permissions
from django_filters.rest_framework import FilterSet, filters
from .models import Service
from .serializers import ServiceSerializer
from apps.accounts.permissions import IsSeller

class ServiceFilter(FilterSet):
    category = filters.CharFilter(field_name="category")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Service
        fields = ["category","is_active"]

class IsSellerOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.seller_id == request.user.id

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.select_related("seller").all()
    serializer_class = ServiceSerializer
    filterset_class = ServiceFilter
    search_fields = ["title","description"]
    ordering_fields = ["price","created_at","delivery_time_days"]
    ordering = ["-created_at"]

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated(), IsSeller()]
        if self.action in ["update","partial_update","destroy"]:
            return [permissions.IsAuthenticated(), IsSeller(), IsSellerOwner()]
        return [permissions.AllowAny()]
