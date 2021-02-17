from collections import UserDict
from typing import Any


class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key: str, value: Any):
        return super().__setitem__(key.lower(), value)

    def __getitem__(self, key: str) -> Any:
        return super().__getitem__(key.lower())

    def __delitem__(self, key: str) -> None:
        return super().__delitem__(key.lower())


class CaseInsensitiveDic(dict):
    def __setitem__(self, key: str, value: Any):
        return super().__setitem__(key.lower(), value)

    def __getitem__(self, key: str) -> Any:
        return super().__getitem__(key.lower())

    def __delitem__(self, key: str) -> None:
        return super().__delitem__(key.lower())


if __name__ == "__main__":
    ci = CaseInsensitiveDict()
    ci["foo"] = "bar"
    ci["BIZ"] = "baz"

    print("FOO:", ci["FOO"])
    print("foo:", ci["foo"])
    print("biz:", ci["FOO"])
    print("BAZ:", ci["foo"])
    del ci["foo"]
    del ci["BIZ"]
