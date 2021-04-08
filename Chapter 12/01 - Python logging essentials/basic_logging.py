import logging

logger = logging.getLogger("my_logger")
logging.basicConfig()

logger.error("This is error message")
logger.warning("This is warning message")
logger.log(logging.CRITICAL, "This is critical message")
