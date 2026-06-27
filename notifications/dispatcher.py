import logging

logger = logging.getLogger(__name__)


class NotificationDispatcher:
    @staticmethod
    def send_email(notification):
        logger.info(f"EMAIL sent: {notification.message}")
        return True

    @staticmethod
    def send_sms(notification):
        logger.info(f"SMS sent: {notification.message}")
        return True

    @staticmethod
    def send_push(notification):
        logger.info(f"PUSH sent: {notification.message}")
        return True

    @staticmethod
    def dispatch(notification):
        return {
            "email": NotificationDispatcher.send_email(notification),
            "sms": NotificationDispatcher.send_sms(notification),
            "push": NotificationDispatcher.send_push(notification),
        }