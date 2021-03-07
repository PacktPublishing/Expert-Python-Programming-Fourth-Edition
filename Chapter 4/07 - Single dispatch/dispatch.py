from datetime import datetime
from functools import singledispatch
from numbers import Real


@singledispatch
def report(value):
    return f"raw: {value}"


@report.register
def _(value: datetime):
    return f"dt: {value.isoformat()}"


@report.register
def _(value: complex):
    return f"complex: {value.real}{value.imag:+}j"


@report.register
def _(value: Real):
    return f"real: {value:f}"


if __name__ == "__main__":
    print(report(datetime.now()))
    print(report(100 - 30j))
    print(report("January"))
    for key, value in report.registry.items():
        print(f"{key} -> {value}")
