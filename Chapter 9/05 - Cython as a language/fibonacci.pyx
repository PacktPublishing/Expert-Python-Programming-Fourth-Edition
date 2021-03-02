"""Cython module that provides fibonacci sequence function."""


cdef long long fibonacci_cc(unsigned int n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_cc(n - 1) + fibonacci_cc(n - 2)


def fibonacci(unsigned int n):
    """ Return nth Fibonacci sequence number computed recursively
    """
    with nogil:
        result = fibonacci_cc(n)

    return fibonacci_cc(n)
