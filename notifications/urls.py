from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import health_check, NotificationViewSet,send_notification
router = DefaultRouter()
router.register(r"notifications", NotificationViewSet, basename="notifications")

urlpatterns = [
    path("health/", health_check),
    path("send/", send_notification),
    path("", include(router.urls)),
]