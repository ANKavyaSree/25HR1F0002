from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer


@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    filterset_fields = ["type"]
    search_fields = ["message"]
    ordering_fields = ["timestamp", "type"]

    def get_queryset(self):
        return Notification.objects.only(
            "id",
            "type",
            "message",
            "timestamp"
        ).order_by("-timestamp")