import logging

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR,
)

sentry_sdk.init(
    dsn="https://<key>:<secret>@app.getsentry.com/<project>",
    integrations=[sentry_logging],
)

try:
    1 / 0
except Exception as e:
    sentry_sdk.capture_exception(e)
