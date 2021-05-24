from abc import ABC, abstractmethod
from typing import Dict


class ViewsStorageBackend(ABC):
    @abstractmethod
    def increment(self, key: str):
        ...

    @abstractmethod
    def most_common(self, n: int) -> Dict[str, int]:
        ...
