LOG_API_URL = "http://20.244.56.144/evaluation-service/logs"

VALID_STACKS = ["backend", "frontend"]

VALID_LEVELS = [
    "debug",
    "info",
    "warn",
    "error",
    "fatal",
]

BACKEND_PACKAGES = [
    "cache",
    "controller",
    "cron_job",
    "db",
    "domain",
    "handler",
    "repository",
    "route",
    "service",
    "auth",
    "config",
    "middleware",
    "utils",
]

FRONTEND_PACKAGES = [
    "api",
    "component",
    "hook",
    "page",
    "state",
    "style",
    "auth",
    "config",
    "middleware",
    "utils",
]