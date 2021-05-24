from datetime import timedelta, datetime
import time
import logging.config
import logging.handlers

import freezegun

logging.config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": (
                    "%(asctime)s | %(levelname)s | "
                    "%(name)s | %(filename)s:%(lineno)d | "
                    "%(message)s"
                )
            },
        },
        "handlers": {
            "logfile": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "formatter": "default",
                "filename": "application.log",
                "when": "D",
                "backupCount": 30,
            }
        },
        "root": {
            "handlers": ["logfile"],
            "level": "INFO",
        },
    }
)

logger = logging.getLogger(__name__)


def main():
    with freezegun.freeze_time() as frozen:
        while True:
            frozen.tick(timedelta(hours=1))
            time.sleep(0.1)
            logger.info(f"Something has happened at {datetime.now()}")


if __name__ == "__main__":
    main()
