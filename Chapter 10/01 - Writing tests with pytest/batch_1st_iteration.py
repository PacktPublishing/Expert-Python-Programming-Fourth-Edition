from typing import Any, Iterable, List


def batches(iterable: Iterable[Any], batch_size: int) -> Iterable[List[Any]]:
    results = []
    batch = []

    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            results.append(batch)
            batch = []

    if batch:
        results.append(batch)

    return results
