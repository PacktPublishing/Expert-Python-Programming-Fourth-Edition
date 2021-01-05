from injector import Module, provider, singleton
from redis import Redis

from interfaces import ViewsStorageBackend
from backends import CounterBackend, RedisBackend


class CounterModule(Module):
    @provider
    @singleton
    def provide_storage(self) -> ViewsStorageBackend:
        return CounterBackend()


class RedisModule(Module):
    @provider
    def provide_storage(self, client: Redis) -> ViewsStorageBackend:
        return RedisBackend(client, "my-set")

    @provider
    def provide_redis_client(self) -> Redis:
        return Redis(host="redis")
