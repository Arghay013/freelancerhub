from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class MyNotificationsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by("-created_at")

class MarkReadView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    def update(self, request, *args, **kwargs):
        n = self.get_object()
        if n.user_id != request.user.id:
            return Response({"detail":"Not allowed."}, status=status.HTTP_403_FORBIDDEN)
        n.is_read = True
        n.save(update_fields=["is_read"])
        return Response({"detail":"Marked as read"})
