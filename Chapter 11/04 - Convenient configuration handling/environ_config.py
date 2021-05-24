from datetime import timedelta
import environ


@environ.config(prefix="")
class Config:
    @environ.config()
    class Bind:
        host = environ.var(default="localhost")
        port = environ.var(default="80", converter=int)

    bind = environ.group(Bind)
    database_uri = environ.var()
    encryption_key = environ.var()

    schedule_interval = environ.var(
        name="SCHEDULE_INTERVAL_SECONDS",
        converter=lambda value: timedelta(seconds=int(value)),
        default=50,
    )


Config.from_environ()
