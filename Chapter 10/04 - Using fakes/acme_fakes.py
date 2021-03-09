from collections import Counter
from typing import Dict


class AcmeHashMapFake:
    def __init__(self):
        self._counter = Counter()

    def atomic_incr(self, key: str, amount):
        self._counter[key] += amount

    def top_keys(self, count: int) -> Dict[str, int]:
        return dict(self._counter.most_common(count))
