from typing import Dict


class AcmeSession:
    def __init__(self, tenant: str, token: str):
        ...


class AcmeHashMap:
    def __init__(self, acme_session: AcmeSession):
        ...

    def incr(self, key: str, amount):
        """Increments any key by specific amount"""

    def atomic_incr(self, key: str, amount):
        """Increments any key by specific amount atomically"""

    def top_keys(self, count: int) -> Dict[str, int]:
        """Returns keys with top values"""
