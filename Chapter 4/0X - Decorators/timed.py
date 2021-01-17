from functools import wraps
from time import time


def timed(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__}() call took {time() -start}s")

    return wrapped


@timed
def sum_2_numbers():
    return sum([1, 2])


@timed
def sum_1000_000_numbers():
    return sum(range(1000_000))


if __name__ == "__main__":
    sum_2_numbers()
    sum_1000_000_numbers()
