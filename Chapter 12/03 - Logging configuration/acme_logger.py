import logging

acme_logger = logging.getLogger("acme.utils")
acme_logger.disabled = True

acme_logger = logging.getLogger("acme.utils")
acme_logger.handlers.clear()

acme_logger = logging.getLogger("acme.utils")
acme_logger.setLevel(logging.CRITICAL)
