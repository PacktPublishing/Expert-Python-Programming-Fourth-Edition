from collections import UserList


class XList(UserList):
    @classmethod
    def double(cls, iterable):
        return cls(iterable) * 2

    @classmethod
    def tripple(cls, iterable):
        return cls(iterable) * 3
