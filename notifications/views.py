from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import NotificationService
from .models import Notification
from .serializers import NotificationSerializer
from logging_middleware import log

log(
    stack="backend",
    level="info",
    package_name="service",
    message="Notification created successfully"
)

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
    


@api_view(["POST"])
def send_notification(request):
    data = request.data

    notification, delivery_status = NotificationService.create_notification(
        notification_type=data["type"],
        message=data["message"],
        timestamp=data["timestamp"],
    )

    return Response({
        "message": "Notification dispatched successfully",
        "id": str(notification.id),
        "delivery_status": delivery_status
    })

