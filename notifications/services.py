from .models import Notification
from .dispatcher import NotificationDispatcher


class NotificationService:
    @staticmethod
    def create_notification(notification_type, message, timestamp):
        notification = Notification.objects.create(
            type=notification_type,
            message=message,
            timestamp=timestamp
        )

        delivery_status = NotificationDispatcher.dispatch(notification)

        return notification, delivery_status