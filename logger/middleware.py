import logging
from .logger import Logger

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJhbmthdnlhc3JpMTFAZ21haWwuY29tIiwiZXhwIjoxNzgyNTM5NzU1LCJpYXQiOjE3ODI1Mzg4NTUsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiI4ZmY5YWM3ZS00YmU1LTQyMGYtYWJjNi04ZTczNWI3MWY4ZjMiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJrYXZ5YSBzcmVlIGFuIiwic3ViIjoiNmU2MjM4YjItYjc0Mi00ZDlkLThmNzAtMThmMzg3YjI2NjQxIn0sImVtYWlsIjoiYW5rYXZ5YXNyaTExQGdtYWlsLmNvbSIsIm5hbWUiOiJrYXZ5YSBzcmVlIGFuIiwicm9sbE5vIjoiMjVocjFmMDAwMiIsImFjY2Vzc0NvZGUiOiJhVGt5YnMiLCJjbGllbnRJRCI6IjZlNjIzOGIyLWI3NDItNGQ5ZC04ZjcwLTE4ZjM4N2IyNjY0MSIsImNsaWVudFNlY3JldCI6InROV1pLd0NIWXZ6UUVBdFIifQ.yNO7AHaJJ6SmLnxKW1gy5ezJI8cWHstFZXhfkVnSRss"


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = Logger(ACCESS_TOKEN)

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        try:
            self.logger.log(
                stack="backend",
                level="error",
                package="middleware",
                message=str(exception)
            )
        except Exception as log_error:
            logging.error(f"Logging failed: {log_error}")

        return None