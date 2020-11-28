import sys

sys.setrecursionlimit(1 << 30)


def crasher():
    return crasher()


crasher()
