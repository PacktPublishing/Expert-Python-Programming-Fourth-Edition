from collections import Counter
from typing import Dict
from redis import Redis

from interfaces import ViewsStorageBackend


class CounterBackend(ViewsStorageBackend):
    def __init__(self):
        self._counter = Counter()

    def increment(self, key: str):
        self._counter[key] += 1

    def most_common(self, n: int) -> Dict[str, int]:
        return dict(self._counter.most_common(n))


class RedisBackend(ViewsStorageBackend):
    def __init__(self, redis_client: Redis, set_name: str):
        self._client = redis_client
        self._set_name = set_name

    def increment(self, key: str):
        self._client.zincrby(self._set_name, 1, key)

    def most_common(self, n: int) -> Dict[str, int]:
        return {
            key.decode(): int(value)
            for key, value in self._client.zrange(
                self._set_name,
                0,
                n - 1,
                desc=True,
                withscores=True,
            )
        }
