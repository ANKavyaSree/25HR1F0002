import requests
from .constants import LOG_API_URL


class LogClient:
    def __init__(self, token):
        self.token = token

    def send_log(self, payload):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(
                LOG_API_URL,
                json=payload,
                headers=headers,
                timeout=3
            )

            print("Log API Status:", response.status_code)
            print("Log API Response:", response.text)

            return response.json()

        except requests.exceptions.RequestException as e:
            print("AffordMed Log Server Error:", e)
            return {
                "success": False,
                "message": "Logging server not reachable"
            }