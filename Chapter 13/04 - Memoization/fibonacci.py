def memoize(function):
    call_cache = {}

    def memoized(argument):
        try:
            return call_cache[argument]
        except KeyError:
            return call_cache.setdefault(argument, function(argument))

    return memoized


@memoize
def fibonacci(n):
    print(f"fibonacci({n})")
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(f"result: {fibonacci(5)=}")
