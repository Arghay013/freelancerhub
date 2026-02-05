from django.urls import path
from .views import SellerDashboardView, BuyerDashboardView

urlpatterns = [
    path("seller/", SellerDashboardView.as_view()),
    path("buyer/", BuyerDashboardView.as_view()),
]
