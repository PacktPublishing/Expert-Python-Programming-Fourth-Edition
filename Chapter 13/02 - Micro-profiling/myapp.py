import time
import tempfile
import cProfile
import pstats


def profile(column="time", list=3):
    def parametrized_decorator(function):
        def decorated(*args, **kw):
            s = tempfile.mktemp()

            profiler = cProfile.Profile()
            profiler.runcall(function, *args, **kw)
            profiler.dump_stats(s)

            p = pstats.Stats(s)
            print("=" * 5, f"{function.__name__}() profile", "=" * 5)
            p.sort_stats(column).print_stats(list)

        return decorated

    return parametrized_decorator


def medium():
    time.sleep(0.01)


@profile("time")
def heavy():
    for i in range(100):
        medium()
        medium()
    time.sleep(2)


@profile("time")
def main():
    for i in range(2):
        heavy()


if __name__ == "__main__":
    main()
