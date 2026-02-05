from django.urls import path
from .views import CreateReviewView, ServiceReviewsView

urlpatterns = [
    path("", CreateReviewView.as_view()),
    path("service/<int:service_id>/", ServiceReviewsView.as_view()),
]
