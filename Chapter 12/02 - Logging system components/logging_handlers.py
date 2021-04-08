from datetime import timedelta, datetime
import time
import logging.handlers

import freezegun


root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    fmt=(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(filename)s:%(lineno)d | "
        "%(message)s"
    )
)
handler = logging.handlers.TimedRotatingFileHandler(
    filename="application.log",
    when="D",
    backupCount=30,
)
handler.setFormatter(formatter)
root_logger.addHandler(handler)


logger = logging.getLogger(__name__)


def main():
    with freezegun.freeze_time() as frozen:
        while True:
            frozen.tick(timedelta(hours=1))
            time.sleep(0.1)
            logger.info(f"Something has happened at {datetime.now()}")


if __name__ == "__main__":
    main()
