from django.urls import path
from .views import PlaceOrderView, MyOrdersView, SellerOrdersView, UpdateOrderStatusView

urlpatterns = [
    path("", PlaceOrderView.as_view()),
    path("my/", MyOrdersView.as_view()),
    path("seller/", SellerOrdersView.as_view()),
    path("<int:pk>/status/", UpdateOrderStatusView.as_view()),
]
