from django.http import JsonResponse
from logger.helper import log


def health_check(request):
    log(
        stack="backend",
        level="info",
        package="controller",
        message="Health endpoint accessed"
    )

    return JsonResponse({"status": "ok"})


def dashboard(request):
    log(
        stack="backend",
        level="info",
        package="controller",
        message="Dashboard accessed"
    )

    return JsonResponse({"message": "Welcome"})