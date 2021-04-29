from typing import Any, Iterable

UNSET = object()


def repr_instance(instance: object, attrs: Iterable[str]):
    attr_values: dict[str, Any] = {
        attr: getattr(instance, attr, UNSET) for attr in attrs
    }
    sub_repr = ", ".join(
        f"{attr}={repr(val) if val is not UNSET else 'UNSET'}"
        for attr, val in attr_values.items()
    )
    return f"<{instance.__class__.__qualname__}: {sub_repr}>"


def autorepr(cls):
    attrs = cls.__annotations__.keys()

    def __repr__(self):
        return repr_instance(self, sorted(attrs))

    cls.__repr__ = __repr__
    return cls


@autorepr
class MyClass:
    attr_a: Any
    attr_b: Any
    attr_c: Any

    def __init__(self, a, b):
        self.attr_a = a
        self.attr_b = b


class MyChildClass(MyClass):
    attr_d: Any

    def __init__(self, a, b):
        super().__init__(a, b)


if __name__ == "__main__":
    print(MyClass("Ultimate answer", 42))
    print(MyClass([1, 2, 3], ["a", "b", "c"]))
    print(MyChildClass("Ultimate answer", 42))
    print(MyChildClass([1, 2, 3], ["a", "b", "c"]))
