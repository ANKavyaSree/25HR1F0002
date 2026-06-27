from .validators import validate_log
from .client import LogClient


class Logger:
    def __init__(self, token):
        self.client = LogClient(token)

    def log(self, stack, level, package, message):
        validate_log(stack, level, package, message)

        payload = {
            "stack": stack,
            "level": level,
            "package": package,
            "message": message,
        }

        return self.client.send_log(payload)