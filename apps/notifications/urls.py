from django.urls import path
from .views import MyNotificationsView, MarkReadView

urlpatterns = [
    path("", MyNotificationsView.as_view()),
    path("<int:pk>/read/", MarkReadView.as_view()),
]
