from typing import Any, Iterable, List
from itertools import islice


def batches(iterable: Iterable[Any], batch_size: int) -> Iterable[List[Any]]:
    iterator = iter(iterable)

    while True:
        batch = list(islice(iterator, batch_size))

        if not batch:
            return

        yield batch
