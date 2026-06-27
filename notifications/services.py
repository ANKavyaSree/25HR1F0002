from .models import Notification


class NotificationService:
    @staticmethod
    def create_notification(notification_type, message, timestamp):
        notification = Notification.objects.create(
            type=notification_type,
            message=message,
            timestamp=timestamp
        )
        return notification

    @staticmethod
    def get_all_notifications():
        return Notification.objects.all().order_by("-timestamp")