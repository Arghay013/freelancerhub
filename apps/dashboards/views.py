from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, Avg
from apps.accounts.permissions import IsSeller, IsBuyer
from apps.services.models import Service
from apps.orders.models import Order
from apps.reviews.models import Review

class SellerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsSeller]
    def get(self, request):
        services = Service.objects.filter(seller=request.user)
        orders = Order.objects.filter(service__seller=request.user)
        earnings = orders.filter(status=Order.Status.COMPLETED).aggregate(total=Sum("service__price"))["total"] or 0
        avg_rating = Review.objects.filter(service__seller=request.user).aggregate(avg=Avg("rating"))["avg"] or 0
        return Response({
            "services_count": services.count(),
            "orders_count": orders.count(),
            "earnings_total": str(earnings),
            "average_rating": float(avg_rating),
        })

class BuyerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsBuyer]
    def get(self, request):
        orders = Order.objects.filter(buyer=request.user)
        reviews = Review.objects.filter(buyer=request.user)
        return Response({
            "orders_count": orders.count(),
            "completed_orders": orders.filter(status=Order.Status.COMPLETED).count(),
            "reviews_left": reviews.count(),
        })
