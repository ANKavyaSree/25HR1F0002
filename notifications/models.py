import uuid
from django.db import models


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ("Result", "Result"),
        ("Placement", "Placement"),
        ("Event", "Event"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )
    message = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["type"]),
            models.Index(fields=["timestamp"]),
        ]

    def __str__(self):
        return f"{self.type} - {self.message[:30]}"