import time
from datetime import timedelta

from freezegun import freeze_time


@freeze_time("1988-02-05 05:10:00")
def test_with_time():
    with freeze_time("1988-02-04 05:10:00") as frozen:
        frozen.move_to("1988-02-05 05:10:00")
        frozen.tick()
        frozen.tick(timedelta(hours=1))

    print(time.time())
    time.sleep(1)
    print(time.time())
    time.sleep(1)
    print(time.time())
    time.sleep(1)
    print(time.time())
    time.sleep(1)
    print(time.time())
